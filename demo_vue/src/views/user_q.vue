<template >
<div class="user_q">

  <div >
    <h3>This is a user {{UserID}} page</h3>
    
    <br><br><br>
    <div class="main">

      <div v-for="item of qdata.length" :key="item" >

          <div class="divTestStyle">
            <fish-field>
              <!-- <label>问题描述{{item+' ：  '+qdata[item-1].q_description+ans[item]}}</label> -->
              <label>问题描述{{item+' ：  '+qdata[item-1].q_description}}</label>
              <fish-select v-model="ans[item-1]">
                <div v-for="count of ansdata[item-1].length" :key="count" :label='item.q_description' :rules="[{ required: true, message: 'not empty'}]" span="24">
                  <fish-option  :index=count  :content=ansdata[item-1][count-1].option_description></fish-option>
                </div>
              </fish-select>  
            </fish-field> 
          </div>
          <br><br><br>
      </div>

      <br><br><br><br><br><br>

      <div>
        <br><br><br>
        <label>一层机制扰动概率：{{sqdata.setQ_pf}}</label><br>
        <label>两层机制扰动概率：{{p2[0]}}</label><br>
        <br><br>
        <label>上次提交</label><br>
        <label>一层机制：{{last_ans1}}</label><br>
        <label>两层机制：{{last_ans2}}</label><br>
        <br><br><br><br>


        <button>您的答案</button>
        <div v-for="item of qdata.length" :key="item" >
          {{ans[item-1]}}
        </div>
        <br><br>

        <button @click="perturb_one" type="submit">一层机制</button>
        <div v-for="item of p1" :key="item[0]" >
          {{item[1]}}
        </div>
        <br><br>

        <button @click="perturb_two" type="submit">两层机制</button>
        <div v-for="item of p2[1]" :key="item[0]" >
          {{item[1]}}
        </div>

      </div>

      <br><br><br>
      <div>
        <button @click="sub" type="submit">提交扰动后的回答</button>
      </div>
    </div>
  </div>
</div>
</template>


<script>
// @ is an alias to /src
import { reactive, ref, OnMounted } from "@vue/composition-api"
import { setq_info , Perturb_One , Perturb_Two , is_existed , first_submit , update_submit } from "../apis/read.js"

export default {
  name: 'user_q',
  components: {
  },
  data() {
    return {
      UserID:'',
      data:[],
      now_setq: 0,
      singleSelectedValue:'',
      sqdata: [],
      qdata: [],
      ansdata: [],
      ans: [],
      p1 : [],
      p2 : [],
      flag : '',
      last_ans1 : [],
      last_ans2 : []
    }
  },
  created() {
    this.now_setq = (ref(this.$route.path)).value.match(/\d+/g)[0];
    this.get_setq()
    this.mem()
  },
  methods: {
    mem(){
      console.log('当前用户id  = ',window.sessionStorage.UserID)
      this.UserID = window.sessionStorage.UserID 
      for(var i = 0; i < 32 ; i++){
          this.$set(this.ans,i,0);
      }
      
    },
    async get_setq(){
        //得到某个问题集合的所有信息
        const param = reactive({
            id : this.now_setq
        });

        console.log(param.id)
        await setq_info(param).then(resp =>{
            this.data = resp.data.data;
            console.log('this.data = ',this.data)
            //data包含sqdata qdata ansdata
            this.sqdata = this.data[0]
            this.qdata = this.data[1];
            this.ansdata = this.data[2];
        });

        const param1 = reactive({
            u_id : this.UserID,
            qlist : []
        });
        for(var i = 0; i < this.qdata.length; i++){
            // console.log(this.qdata[i].idq)
            param1.qlist[i] = this.qdata[i].idq
        }
        console.log('qlist = ',param1.qlist)
        is_existed(param1).then(resp =>{
            console.log('查询结果',resp.data.data)
            //这里加一个flag判断
            console.log('长度',resp.data.data.length)
            if( resp.data.data.length != 0){
              this.flag = false
              for(var i = 0; i < resp.data.data.length; i ++){
                // console.log(resp.data.data[i])
                this.last_ans1[i] = resp.data.data[i].ans_one
                this.last_ans2[i] = resp.data.data[i].ans_two
              }
            }
            else{
              this.flag = true
            }
        });
    },
    sub(){
        for(var i = 0; i < this.qdata.length; i++){
          console.log('问题',i+1,'原始答案',this.ans[i]);
        }
        const param = {
          id_user : this.UserID,
          qlist : [],
          ans1 : [],
          ans2 : [],
        }
        for(var i = 0; i < this.qdata.length; i++){
            param.qlist[i] = this.qdata[i].idq
            param.ans1[i] = this.p1[i][1]
            param.ans2[i] = this.p2[1][i][1]
        }
        //判断要不要更新用户的回答
        console.log('this.flag = ',this.flag)

        if (this.flag == true){
          first_submit(param).then(resp =>{
              console.log(resp.data.data)
              //这里加上判断是否添加成功，刷新页面
              // if(resp.data.resCode == 0){
              //   alert('提交成功！')
              //   this.$router.push({
              //     path:'/user_q/'+ this.sqdata.idsetQ
              //   });
              // }
              // else{
              //   alert('提交失败，请重新尝试！')
              //   this.$router.push({
              //     path:'/user_q/'+ this.sqdata.idsetQ
              //   });
              // }
          })
        }
        else{
          update_submit(param).then(resp =>{
              console.log(resp.data.data)
              //这里加上判断是否添加成功，刷新页面
              // console.log(resp.data.resCode)
          })
        }



    },
    perturb_one(){
        const ans_list = [];
        const id_setq = this.sqdata.idsetQ;
        // const pf = this.sqdata.setQ_pf;
        for(var i = 0; i < this.qdata.length; i++){
          const tmp = [];
          tmp[0] = this.qdata[i].idq
          tmp[1] = this.ans[i]
          ans_list[i] = tmp;
        }
        console.log(id_setq,ans_list)
        const param = {
          id : id_setq,
          // pf : pf,
          ans : ans_list
        }
        Perturb_One(param).then(resp =>{
          console.log(resp.data.data)
          this.p1 = resp.data.data
        });
    },

    perturb_two(){
        const ans_list = [];
        const id_setq = this.sqdata.idsetQ;
        // const pf = this.sqdata.setQ_pf;
        for(var i = 0; i < this.qdata.length; i++){
          const tmp = [];
          tmp[0] = this.qdata[i].idq
          tmp[1] = this.ans[i]
          ans_list[i] = tmp;
        }
        console.log(id_setq,ans_list)
        const param = {
          id : id_setq,
          // pf : pf,
          ans : ans_list
        }
        Perturb_Two(param).then(resp =>{
          console.log(resp.data.data)
          this.p2 = resp.data.data
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
.user_q{
  width: 100%;
  height: 100%;
  border: 3px solid rgb(255, 255, 255);
  background-color: rgb(255, 255, 255);
}
.divTestStyle{
  font-size: 15px;
  width: 800px;
  height: 80px;
  text-align: center;
  position: center;
  border: 2px solid #81c2a5;
  border-radius: 10px;
  
}
.main{
  
    text-align: center; /*让div内部文字居中*/
    background-color: rgb(255, 255, 255);
    border-radius: 15px;
    width: 800px;
    height: 800px;
    margin: auto;
    position: center;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
}


</style>