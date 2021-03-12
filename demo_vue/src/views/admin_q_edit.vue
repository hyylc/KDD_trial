<template>
  <div class="admin_q_edit">
    <div id="app">
      <div id="nav">
     <!--<router-link to="/user_home">问卷列表</router-link> |
        <router-link to="/about">个人信息</router-link><br><br> -->
        <ul>
            <li><a href="/admin_home">问卷列表</a></li>
            <li><a class="active" href="/admin_q_edit">发布问卷</a></li>
        </ul>
        <fish-form ref="form" >
        <fish-fields >
            <fish-field label="问卷标题" span="20" name="setq_title" :rules="[{ required: true, message: 'not empty'}]">
                <fish-input v-model="setq_des"></fish-input>
            </fish-field>
            <fish-field label="问题数量" span="2" name="setq_num" :rules="[{ required: true, message: 'not empty'}]">
                <fish-input-number min="-1" max="30" v-model="setq_q_num"></fish-input-number>
            </fish-field>
        </fish-fields>
        <fish-fields >
            <fish-field label="one-layer mechanism参数设置：扰动概率pf" span="10" name="setq_pf" :rules="[{ required: true, message: 'not empty'}]">
                <fish-input-number min="-0.01" max="0.55" step="0.05" v-model="setq_pf"></fish-input-number>
            </fish-field>
            <fish-field label="two-layer mechanism参数设置：均匀分布参数b（默认是pf的两倍）" span="10" name="setq_b" :rules="[{ required: true, message: 'not empty'}]">
                <fish-input-number min="-0.01" max="1.10" step="0.1" v-model="setq_b"></fish-input-number>
            </fish-field>
        </fish-fields>
        <div v-for="count of setq_q_num" :key="count"> 
            <fish-fields>
                <fish-field label="Q问题描述" span="15" name="q_title" :rules="[{ required: true, message: 'not empty'}]">
                    <fish-input v-model="q_list[count].des"></fish-input>
                </fish-field>
                <fish-field label="Q选项数量" span="2" name="q_num" :rules="[{ required: true, message: 'not empty'}]">
                    <fish-input-number min="-1" max="30" v-model="q_list[count].num"></fish-input-number>
                </fish-field>
            </fish-fields>
            <div v-for="count1 of q_list[count].num" :key="count1"> 
                <fish-field label="option" span="10" name="q_ans" :rules="[{ required: true, message: 'not empty'}]">
                    <fish-input span="10" v-model="q_list[count].ans_list[count1]"></fish-input>
                </fish-field>
            </div>  
        </div>
    </fish-form> 
    </div > 
  </div>
    <button @click="print_qlist" type="submit">打印</button>
    <button @click="publish" type="submit">发布该问卷</button>
  </div>
</template>


<script>
// @ is an alias to /src
import { new_setq, new_q, new_option } from "../apis/read.js";//从apis中引入，通过这个请求拿到数据
import { reactive, ref, onMounted } from "@vue/composition-api"


export default {
  name: 'admin_q_edit',
  components: {
  },
    data() {
        return {
            data: [],
            setq_q_num: 0,
            q_list: [],
            age:'',
            setq_des: '',
            setq_pf: 0.0,
            setq_b: 0.0,
        }
    },
    watch:{
        //监听
        'setq_pf' : {
            handler(){
                this.setq_b = this.setq_pf * 2;
            }
        },
        'setq_b' : {
            handler(){
                this.setq_pf = this.setq_b / 2;
            }
        }
    },
    created() {
        this.mem();
        this.setq_b = this.setq_pf*2;
    },
    methods: {
        
        mem(){
            for(var i = 0; i < 31; i++){
                //使用set初始化，使数组数据成为响应式，可以实时监测
                //或者使用watch的方法
                this.$set(this.q_list,i,{ num: 0, des: '',ans_list: []});
                for(var j = 0; j < 31; j++){
                    this.q_list[i].ans_list[j] = ''
                } 
            };
        },

        print_qlist(){
            console.log('问题选项列表 ',this.q_list);
            console.log('问题数 ',this.setq_q_num);
        },

        publish(){

            //新建一个问题集合，添加信息如  （问题描述，参数pf，参数b）
            //获得添加的问题id，便于后面添加问题
            const param = reactive({
                desc : this.setq_des,
                pf : this.setq_pf,
                b : this.setq_b
            });

            const resdata = reactive({});
            const is_setq_add = reactive({});
            const resdata1 = reactive({});
            const is_q_add = reactive({});
            const resdata2 = reactive({});
            const is_op_add = reactive({});




            new_setq(param).then(resp =>{
                console.log('new setq 接口调用')
                this.resdata = resp.data.data;
                console.log(this.resdata);
                this.is_setq_add = false;
                if(this.resdata.length == 0){
                    alert(resp.data.message)
                }
                else{
                    this.is_setq_add = true;
                    
                    for(var i=1; i<=this.setq_q_num; i++){
                        const param1 = reactive({
                            setq_id : this.resdata,
                            desc : this.q_list[i].des,
                            num : this.q_list[i].num,
                        });
                        this.index = 1;
                        new_q(param1).then(resp1 =>{
                            console.log('new q 接口调用')
                            this.resdata1 = resp1.data.data;
                            console.log(this.resdata1);
                            this.is_q_add = false;
                            
                            if(this.resdata1.length == 0){
                                alert(resp1.data.message)
                            }

                            else{
                                this.is_q_add = true;
                                console.log('this.is_q_add = ',this.is_q_add)
                                console.log('i = ',i,'q_list[i].num = ',this.q_list[this.index].num)
                                for(var j=1; j<=this.q_list[this.index].num; j++){
                                    
                                    const param2 = reactive({
                                        q_id : this.resdata1,
                                        desc : this.q_list[this.index].ans_list[j],
                                        num : j,
                                    });
                                    console.log('待插入选项',param2)

                                    new_option(param2).then(resp2 =>{
                                        console.log('new option 接口调用')
                                        this.resdata2 = resp2.data.data;
                                        console.log(this.resdata2);
                                        this.is_op_add = false;
                                        if(this.resdata2.length == 0){
                                            alert(resp1.data.message)
                                        }
                                        else{
                                            this.is_op_add = true;
                                        }
                                    }).catch(err =>{
                                        console.log(err)
                                    });
                                }
                            }
                        }).catch(err =>{
                            console.log(err)
                        });
                    }
                }
            }).catch(err =>{
                console.log(err)
            });
        },
    }
}

</script>

<style scoped lang="scss">
h3 {
  font-size: 30px;
  margin: 40px 0 0;
}
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    border: 1px solid #e7e7e7;
    background-color: #f3f3f3;
}

li {
    float: left;
}

li a {
    display: block;
    color: #666;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

li a:hover:not(.active) {
    background-color: #ddd;
}

li a.active {
    color: white;
    background-color:#42b983;
}

</style>