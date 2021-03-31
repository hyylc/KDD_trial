<template >
<div class="user_q">

  <div >
    <h3>This is a user_q page</h3>
    <br><br><br>
    <div class="main">

      <div v-for="item of qdata.length" :key="item" >

          <div class="divTestStyle">
            <fish-field>
              <!-- <label>问题描述{{item+' ：  '+qdata[item-1].q_description+ans[item]}}</label> -->
              <label>问题描述{{item+' ：  '+qdata[item-1].q_description}}</label>
              <fish-select v-model="ans[item]">
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
        <label>上次提交：一层机制：{{sqdata.setQ_pf}}</label><br>
        这里打印结果（如果没提交过，就显示没有好了）
        <br><br>
        <label>上次提交：两层机制：{{sqdata.setQ_pf}}</label><br>
        这里打印结果
        <br><br><br><br>


        <button @click="perturb_one" type="submit">一层机制</button>
        这里打印扰动的结果
        <div v-for="item of p1" :key="item[0]" >
          {{item[1]}}
        </div>
        <br><br>
        <button @click="perturb_two" type="submit">两层机制</button>
        这里打印扰动的结果
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
import { setq_info , Perturb_One , Perturb_Two } from "../apis/read.js"

export default {
  name: 'user_q',
  components: {
  },
  data() {
    return {
      data:[],
      now_setq: 0,
      singleSelectedValue:'',
      sqdata: [],
      qdata: [],
      ansdata: [],
      ans: [],
      p1 : [],
      p2 : []
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
      for(var i = 0; i < 32 ; i++){
          this.$set(this.ans,i,0);
      }
    },
    get_setq(){
      //得到某个问题集合的所有信息
      const param = reactive({
          id : this.now_setq
      });

      console.log(param.id)
      setq_info(param).then(resp =>{
          this.data = resp.data.data;
          console.log('this.data = ',this.data)
          //data包含sqdata qdata ansdata
          this.sqdata = this.data[0]
          this.qdata = this.data[1];
          this.ansdata = this.data[2];
      });
      
    },
    sub(){
        for(var i = 1; i <= this.qdata.length; i++){
          console.log('问题',i,'结果',this.ans[i]);
        }

        //可能要更新用户的回答




    },
    perturb_one(){
        const ans_list = [];
        const id_setq = this.sqdata.idsetQ;
        // const pf = this.sqdata.setQ_pf;
        for(var i = 1; i <= this.qdata.length; i++){
          const tmp = [];
          tmp[0] = this.qdata[i-1].idq
          tmp[1] = this.ans[i]
          ans_list[i-1] = tmp;
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
        for(var i = 1; i <= this.qdata.length; i++){
          const tmp = [];
          tmp[0] = this.qdata[i-1].idq
          tmp[1] = this.ans[i]
          ans_list[i-1] = tmp;
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