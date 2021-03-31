import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
      bodyWidth: 0,
      bodyHeight: 0,
  },
  mutations: {
    height(state, n) {
      state.bodyHeight = n + 7
    },
    width(state, n) {
    state.bodyWidth = n
  },
},
  actions: {

  }
})
