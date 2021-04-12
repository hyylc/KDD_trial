<template>
  <div class="about">
    <div id="app">
    <div id="nav">
      <br><br><br><br><br><br>
      <router-link to="/home">登录</router-link> |
      <router-link to="/about">注册</router-link><br><br>
      <input  v-model="user.username" type="text"  placeholder="用户名" ><br><br>
      <input  v-model="user.password" type="password"  placeholder="密码" ><br><br><br>
      <button @click="register" type="submit" class="button orange">注册</button>
    </div>
    <router-view/>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { sign_up } from "../apis/read.js";//从apis中引入，通过这个请求拿到数据

export default {
  name: 'about',
  components: {
  },
  data() {
    return {
      data:[],
      user:{
        username : '',
        password : ''
      }
    }
  },
  created() {
    
  },
  methods: {
    register(){
      console.log("输入的用户名和密码",this.user)
      sign_up(this.user).then(resp => {
        console.log("In register resp = ",resp);
				console.log("In register resp.data.message = ",resp.data.message)
        if (resp.data.resCode == 0){
          ///注册成功,转换到登录
          alert('注册成功！');
          this.$router.push({
						path:'/home',
					});
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

<style scoped lang="scss">
h3 {
  font-size: 30px;
  margin: 40px 0 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>