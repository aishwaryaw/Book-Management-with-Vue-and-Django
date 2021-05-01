import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Element from 'element-ui'
import axios from 'axios';

Vue.config.productionTip = false
Vue.use(Element)
// axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.baseURL = 'https://https://book-management-vue-django.herokuapp.com/'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
