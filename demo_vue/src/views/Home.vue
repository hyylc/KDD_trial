<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
   <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
   <button @click="register" type="submit">注册</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import { sign_up } from "../apis/read.js";//从apis中引入，通过这个请求拿到数据

export default {
  name: 'home',
  components: {
    HelloWorld
  },
  data() {
    return {
      data:[],
    }
  },
  created() {
  },
  methods: {
    register(){
      sign_up().then(resp => {
        console.log("In register resp = ",resp);
				console.log("In register resp.data.message = ",resp.data.message)
        if (resp.data.resCode == 0){
          ///注册成功,转换到登录
          alert('注册成功！');
        }
        else{
          //停留在当前页面
          alert('注册失败。');
        }
      });
    }
  }
}
</script>
