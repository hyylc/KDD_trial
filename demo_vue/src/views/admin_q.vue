<template>

<body style="100%">
  <div id="admin_q">
    <h1 class="header"> {{AdminID}}</h1>
    <div class="container">
      <div class="left"></div>
      <div class="main"></div>
    </div>
  </div>
</body>
</template>


<script>
import { reactive, ref, OnMounted } from "@vue/composition-api"
import { setq_info , Perturb_One , Perturb_Two , is_existed , first_submit , update_submit } from "../apis/read.js"

export default {
  name: 'user_q',
  components: {
  },
  data() {
    return {
      AdminID:'',
      data:[],
      now_setq: 0,
      sqdata: [],
      qdata: [],
      ansdata: [],
      
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
        });
    },
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
      /* height:  100%; */
    }
    .left {
      background-color: lightgreen;
      float: left;
      flex: 3;
    }
    .main {
      background-color: lightpink;
      float: right;
      flex: 7;
    }
    



</style>