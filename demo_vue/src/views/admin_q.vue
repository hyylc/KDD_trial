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
        <div class="main1">这里打印用户的回答或者打印以前聚合的结果
        </div>
        <div class="main2">
            <label>
              <br>
              <button class="divTestStyle2" @click="project_Aggregate" type="submit">当前该问卷有xxx份提交记录，点击按钮获取结果。</button>
              <br><br>
              <label class="divTestStyle1" type="submit">MV-One</label>
              <br>
              <label class="divTestStyle1" type="submit">MV-Two</label>
              <br>
              <label class="divTestStyle1" type="submit">TD-One</label>
              <br>
              <label class="divTestStyle1" type="submit">TD-Two</label>
            </label>
        </div>
      </div>
    </div>
  </div>
</body>
</template>


<script>
import { reactive, ref, OnMounted } from "@vue/composition-api"
import { setq_info , Aggregate} from "../apis/read.js"

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
    },
    project_Aggregate(){
        const param = {
          id_setq : this.now_setq
        }
        Aggregate(param).then(resp =>{
          console.log(resp.data.data)
        })
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
      color-interpolation-filters: auto;
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
      height: 60%;
      background-color: rgb(251, 202, 210);
      float: right;
      flex: 7;
    }
    .main2 {
      height: 40%;
      background-color: rgb(228, 115, 134);
      float: right;
      flex: 7;
    }
    .divTestStyle1{
      font-size: 12px;
      height: 10%;
      text-align: center;
      position: relative;
      border: 2px solid #da6758;
      background-color: #eec8c8;
      padding-left: 5mm;
      padding-right: 5mm;
      border-radius: 10px;
      border-left: 1cm;
      left: 30%;
    }
      .divTestStyle2{
      font-size: 18px;
      height: 10%;
      text-align: center;
      position: relative;
      background-color: #eec8c8;
      left: 20%;
    }
    


</style>