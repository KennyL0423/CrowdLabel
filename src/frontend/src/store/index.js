import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : '',
    TaskID: localStorage.getItem('TaskID') ? localStorage.getItem('TaskID'): '',
  },
  getters: {
  },
  mutations: {
      changeLogin (state, value) {
        state.Authorization = value;
        localStorage.setItem('Authorization', value)
      },
      changeTaskID (state, value) {
        state.TaskID = value;
        localStorage.setItem('TaskID', value)
      },
      removeStorage (state) {
        localStorage.removeItem('Authorization');
      }
  },
  actions: {
  },
  modules: {
  }
})
