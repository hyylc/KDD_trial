<template>
  <div class="user_info">
    <div id="app">
      <div id="nav">
        <ul>
            <li><a href="/user_home">问卷列表</a></li>
            <li><a class="active" href="/user_info">个人信息</a></li>
        </ul>
      </div>
      <router-view/>
    </div >
  </div>
  
</template>


<script>
// @ is an alias to /src

export default {
  name: 'user_info',
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
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    border: 1px solid #e7e7e7;
    background-color: #f3f3f3;
}

li {
    float: left;
}

li a {
    display: block;
    color: #666;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

li a:hover:not(.active) {
    background-color: #ddd;
}

li a.active {
    color: white;
    background-color:#42b983;
}
</style>