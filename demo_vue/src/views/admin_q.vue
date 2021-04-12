<template>

<body style="100%">
  <div id="admin_q">
    <h1 class="header"> {{AdminID}}</h1>
    <div class="container">
      <div class="left">
        <!-- 这里展示问题集合的信息 -->
        <!-- {{this.q_info}} -->
        <fish-table :columns="this.columns" :data="data" :pagination="page" ></fish-table>
      </div>
      <div class="main">
        <div class="main1">这里打印用户的回答
          <!-- <div>
          <fish-select v-model="singleSelectedValue" class="divTestStyle1">
            <fish-option index="0" content="Option-1"></fish-option>
          </fish-select>
          </div> -->
        </div>
        <div class="main2"></div>
      </div>
    </div>
  </div>
</body>
</template>


<script>
import { reactive, ref, OnMounted } from "@vue/composition-api"
import { setq_info } from "../apis/read.js"

export default {
  name: 'admin_q',
  components: {
  },
  data() {
    return {
      AdminID:'',
      data:[],
      singleSelectedValue: '',
      now_setq: 0,
      sqdata: [],
      qdata: [],
      ansdata: [],
      page: {total: 0, current: 1},
      columns: [
        {title: '问题编号', key: 'id'},
        {title: '问题描述', key: 'desc'},
      ],
      q_info: '',
      
    }
  },
  created() {
    this.now_setq = (ref(this.$route.path)).value.match(/\d+/g)[0];
    this.get_setq()

  },
  methods: {
    async get_setq(){
        this.AdminID = window.sessionStorage.AdminID 

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
            for (let i=0; i < this.qdata.length; i++){
              this.data[i] = {
                id : '',
                desc : ''
              }
              this.data[i].id = this.qdata[i].idq;
              this.data[i].desc = this.qdata[i].q_description;
            }
            this.page.total = this.qdata.length;
        });
    },
    q_detail(q){
      console.log('待查询的问题id = ', q)
    }
  }
}
</script>

<style>
    body {
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
    }
    div{
        width:100%;
        height: 100%;
    }
    .header {
      background-color: orange;
      height: 80px;
    }
    h1 {
      margin: 0;
      padding: 0;
      font-size: 16px;
    }
    .container {
      /* margin: 0; */
      padding: 0;
      display: flex;
      position: relative;
      /* height: 800px; */
      /* width: 100%; */
      height:  100%;
    }
    .left {
      border-color: lightgreen;
      height: 100%;
      background-color: lightgreen;
      float: left;
      flex: 3;
    }
    .main {
      height: 100%;
      background-color: lightpink;
      float: right;
      flex: 7;
    }
    .main1 {
      height: 80%;
      background-color: rgb(251, 202, 210);
      float: right;
      flex: 7;
    }
    .main2 {
      height: 20%;
      background-color: rgb(228, 115, 134);
      float: right;
      flex: 7;
    }
    .divTestStyle1{
      font-size: 12px;
      height: 10%;
      text-align: center;
      position: center;
      border: 2px solid #81c2a5;
      border-radius: 10px;
    }


</style>