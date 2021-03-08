<template>
  <div class="user_home">
    <h3>This is a user_home page</h3>
  </div>
</template>


<script>
// @ is an alias to /src
import { sign_up } from "../apis/read.js";//从apis中引入，通过这个请求拿到数据

export default {
  name: 'user_home',
  components: {
  },
  data() {
    return {
      data:[]
    }
  },
  created() {
    
  },
  methods: {

  }
}
</script>

<style scoped lang="scss">
h3 {
  font-size: 30px;
  margin: 40px 0 0;
}
</style>