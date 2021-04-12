<template>
  <div class="home">
    <div id="app">
    <div id="nav">
      <br><br><br><br><br><br>
      <router-link to="/home">登录</router-link> |
      <router-link to="/about">注册</router-link><br><br>
      <input  v-model="user.username" type="text"  placeholder="用户名" ><br><br>
      <input  v-model="user.password" type="password"  placeholder="密码" ><br><br><br>
      <button @click="register" type="submit" class="button orange">用户登录</button>
      <button @click="register_admin" type="submit" class="button orange">管理员登录</button>
    </div>
    <router-view/>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import { sign_in , sign_in_admin } from "../apis/read.js";//从apis中引入，通过这个请求拿到数据

export default {
  name: 'home',
  components: {
    HelloWorld
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
      sign_in(this.user).then(resp => {
        console.log("In register resp = ",resp);
				console.log("In register resp.data.message = ",resp.data.message);
        if (resp.data.resCode == 0){
          window.sessionStorage.setItem('UserID',resp.data.data.iduser);
          console.log('当前用户id ',window.sessionStorage.UserID);
          alert('登录成功！');
          //UserID保持到窗口关闭
          //跳转用户首页
          this.$router.push({
						path:'/user_home'
					});
        }
        else{
          alert('登录失败。');
        }
      });
    },

    register_admin(){
      console.log("输入的用户名和密码",this.user)
      sign_in_admin(this.user).then(resp => {
        console.log("In register resp = ",resp);
				console.log("In register resp.data.message = ",resp.data.message);
        if (resp.data.resCode == 0){
          window.sessionStorage.setItem('AdminID',resp.data.data.idadmin);
          console.log('当前用户id ',window.sessionStorage.AdminID);
          alert('登录成功！');
          //UserID保持到窗口关闭
          //跳转用户首页
          this.$router.push({
						path:'/admin_home'
					});
        }
        else{
          alert('登录失败。');
        }
      });
    },
  }
}
</script>

<style lang="scss">
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

// body {
//  background: #ededed;
//  width: 900px;
//  margin: 30px auto;
//  color: #999;
// }
// p {
//  margin: 0 0 2em;
// }
// h1 {
//  margin: 0;
// }
// a {
//  color: #339;
//  text-decoration: none;
// }
// a:hover {
//  text-decoration: underline;
// }
// div {
//  padding: 20px 0;
//  border-bottom: solid 1px #ccc;
// }

.button {
 display: inline-block;
 zoom: 1; /* zoom and *display = ie7 hack for display:inline-block */
 *display: inline;
 vertical-align: baseline;
 margin: 0 2px;
 outline: none;
 cursor: pointer;
 text-align: center;
 text-decoration: none;
 font: 14px/100% Arial, Helvetica, sans-serif;
 padding: .5em 2em .55em;
 text-shadow: 0 1px 1px rgba(0,0,0,.3);
 -webkit-border-radius: .5em; 
 -moz-border-radius: .5em;
 border-radius: .5em;
 -webkit-box-shadow: 0 1px 2px rgba(0,0,0,.2);
 -moz-box-shadow: 0 1px 2px rgba(0,0,0,.2);
 box-shadow: 0 1px 2px rgba(0,0,0,.2);
}
.button:hover {
 text-decoration: none;
}
.button:active {
 position: relative;
 top: 1px;
}
  
.bigrounded {
 -webkit-border-radius: 2em;
 -moz-border-radius: 2em;
 border-radius: 2em;
}
.medium {
 font-size: 12px;
 padding: .4em 1.5em .42em;
}
.small {
 font-size: 11px;
 padding: .2em 1em .275em;
}

/* orange */
.orange {
 color: #fef4e9;
 border: solid 1px #da7c0c;
 background: #f78d1d;
 background: -webkit-gradient(linear, left top, left bottom, from(#faa51a), to(#f47a20));
 background: -moz-linear-gradient(top,  #faa51a,  #f47a20);
 filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#faa51a', endColorstr='#f47a20');
}
.orange:hover {
 background: #f47c20;
 background: -webkit-gradient(linear, left top, left bottom, from(#f88e11), to(#f06015));
 background: -moz-linear-gradient(top,  #f88e11,  #f06015);
 filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#f88e11', endColorstr='#f06015');
}
.orange:active {
 color: #fcd3a5;
 background: -webkit-gradient(linear, left top, left bottom, from(#f47a20), to(#faa51a));
 background: -moz-linear-gradient(top,  #f47a20,  #faa51a);
 filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#f47a20', endColorstr='#faa51a');
}
</style>