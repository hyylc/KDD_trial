<template>
  <div class="user_home">
    <div id="app">
      <div id="nav">
        <ul>
            <li><a class="active" href="/user_home">问卷列表</a></li>
            <li><a href="/user_info">个人信息</a></li>
        </ul>
        <fish-table :columns="columns" :data="data" :pagination="page" ></fish-table>
    </div > 
  </div>
 
  </div>
</template>


<script>
// @ is an alias to /src
import { get_all_setq } from "../apis/read.js";//从apis中引入，通过这个请求拿到数据
import React from 'react'
import { Redirect } from 'react-router-dom'

export default {
  name: 'user_home',
  components: {
  },
  data() {
    return {
        page: {total: 0, current: 1},
        columns: [
          {title: '问卷编号', key: 'id'},
          {title: '问卷描述', key: 'desc'},
          {title: '操作', key: 'operate',
            render: (h, record, column) => {
              console.log(this.now_setq)
              record.id = '/user_q/'+record.id
              return <router-link to={record.id}>查看详情</router-link>
            }
          }
        ],
        data: [],
        now_setq: 0,
        now_user: 0,

    }
  },
  created() {
    this.get_setq();
  },
  methods: {
    get_setq(){
        console.log('当前用户id  = ',window.sessionStorage.UserID)
        get_all_setq().then(resp => {
            console.log("In register resp = ",resp);
            console.log("In register resp.data.message = ",resp.data.message);
            this.data = resp.data.data;
            console.log('输出结果 = ',this.data)
            for (var i=0; i < resp.data.data.length; i++){
              this.data[i].id = resp.data.data[i].idsetQ;
              this.data[i].desc = resp.data.data[i].setQ_description;
            }
            this.page.total = resp.data.data.length;
            if(this.data.length == 0){
                alert('暂无问卷数据。')
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