<template>
  <div class="admin_home">
    <div id="app">
      <div id="nav">
     <!--<router-link to="/user_home">问卷列表</router-link> |
        <router-link to="/about">个人信息</router-link><br><br> -->
        <ul>
            <li><a class="active" href="/admin_home">问卷列表</a></li>
            <li><a href="/admin_q_edit">发布问卷</a></li>
        </ul>
        <fish-table :columns="columns" :data="data" :pagination="page" ></fish-table>
    </div > 
  </div>
 
  </div>
</template>


<script>
// @ is an alias to /src
import { get_all_setq } from "../apis/read.js";//从apis中引入，通过这个请求拿到数据

export default {
  name: 'admin_home',
  components: {
  },
  data() {
    return {
        page: {total: 15, current: 1},
        columns: [{title: 'Name', key: 'name'},
          {title: 'age', key: 'age'},
          {title: 'Address', key: 'address'},
          {title: 'Operate',
            key: 'operate',
            render: (h, record, column) => h('a', '编辑')}],
        data: [
          
        ]
    }
  },
  created() {
    this.get_setq();
  },
  methods: {
    get_setq(){
        get_all_setq().then(resp => {
            console.log("In register resp = ",resp);
            console.log("In register resp.data.message = ",resp.data.message);
            this.data = resp.data.data;
            console.log('输出结果 = ',this.data)
            // if(this.data.length == 0){
            //     alert('暂无问卷数据。')
            // }
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