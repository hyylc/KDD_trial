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
                <fish-input-number min="0" max="30" v-model="setq_q_num"></fish-input-number>
            </fish-field>
        </fish-fields>
        <div v-for="count of setq_q_num" :key="count"> 
            <fish-fields>
                <fish-field label="Q问题描述" span="15" name="q_title" :rules="[{ required: true, message: 'not empty'}]">
                    <fish-input v-model="q_list[count].des"></fish-input>
                </fish-field>
                <fish-field label="Q选项数量" span="2" name="q_num" :rules="[{ required: true, message: 'not empty'}]">
                    <fish-input-number min="0" max="30" v-model="q_list[count].num"></fish-input-number>
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
import { get_all_setq } from "../apis/read.js";//从apis中引入，通过这个请求拿到数据

export default {
  name: 'admin_q_edit',
  components: {
  },
  data() {
    return {
        data: [],
        setq_des: '',
        setq_q_num: 0,
        q_list: [],
        age:''
    }
  },
  created() {
      this.mem()
  },
  methods: {
      mem(){
          for(var i = 0; i < 31; i++){
              //使用set初始化，使数组数据成为响应式，可以实时监测
              //好像还有使用watch的方法
              this.$set(this.q_list,i,{ num: 0, des: '',ans_list: []});
              for(var j = 0; j < 31; j++){
                  this.q_list[i].ans_list[j] = ''
              }
              
          };
      },
      print_qlist(){
          console.log(this.q_list);
          console.log(this.setq_q_num)
      },
      publish(){
          
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