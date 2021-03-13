<template>
  <div class="user_q">
    <h3>This is a user_q page</h3>
    <br><br><br><br><br><br>
    <!-- <div v-for="count of setq_q_num" :key="count">  -->
    <div class="main">
      <div class="divTestStyle">
        <div v-for="item of qdata.length" :key="item" >
          <fish-field>
            <label>{{qdata[item-1].q_description}}</label>
            <fish-select >
              <div v-for="count of ansdata[item-1].length" :key="count" :label='item.q_description' span="24">
                <fish-option :index=count :content=ansdata[item-1][count-1].option_description></fish-option>
              </div>
            </fish-select>  
          </fish-field> 
        </div>
      </div>
    </div>
  </div>
  <!-- </div> -->
</template>


<script>
// @ is an alias to /src
import { reactive, ref, OnMounted } from "@vue/composition-api"
import { setq_info } from "../apis/read.js"

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
    }
  },
  created() {
    this.now_setq = (ref(this.$route.path)).value.match(/\d+/g)[0];
    this.get_setq()
  },
  methods: {
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
      
    }
  }
}
</script>

<style scoped lang="scss">
h3 {
  font-size: 30px;
  margin: 40px 0 0;
}
.divTestStyle{
  width: 300px;
  height: 80px;
  text-align: center;
  border: 3px solid blue;
}
.main{
    text-align: center; /*让div内部文字居中*/
    background-color: #fff;
    border-radius: 20px;
    width: 300px;
    height: 350px;
    margin: auto;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
}

</style>