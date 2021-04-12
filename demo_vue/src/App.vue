<template>
<div id="app">
    <router-view v-if="isRouterAlive"></router-view>
  </div>
  <!-- <div id="app">
    <div id="nav">
      <br><br><br><br><br><br>
      <router-link to="/">登录</router-link> |
      <router-link to="/about">注册</router-link>
    </div>
    <router-view/>
  </div> -->
</template>

<script>
export default {
  name: 'app',
  provide (){
    return {
      reload : this.reload
    }
  },
  data (){
    return {
      isRouterAlive : true
    }
  },
  methods: {
    reload (){
      this.isRouterAlive = false
      this.$nextTick(function(){
        this.isRouterAlive = true
      })
    }
  }
}
</script>
<style lang="scss">
// #app {
//   font-family: 'Avenir', Helvetica, Arial, sans-serif;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
//   text-align: center;
//   color: #2c3e50;
// }
// #nav {
//   padding: 30px;
//   a {
//     font-weight: bold;
//     color: #2c3e50;
//     &.router-link-exact-active {
//       color: #42b983;
//     }
//   }
// }
</style>
