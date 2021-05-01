import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import EditBook from '../views/EditBook.vue'
import CreateBook from '../views/CreateBook.vue'
import NotFoundComponent from '../components/NotFoundComponent.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { layout: true }
  },
  {
    path: '/login',
    name: 'Login',
    component : Login,
    meta: { layout: true }
  },
  {
    path: '/register',
    name: 'Register',
    component : Register,
    meta: { layout: true }
  },
  {
    path: '/book/edit/:bookId',
    name: 'EditBook',
    component : EditBook,
    meta: { layout: true }
  },
  {
    path: '/create/book',
    name: 'CreateBook',
    component : CreateBook,
    meta: { layout: true }
  },
   { 
    path: "/:pathMatch(.*)*", 
    component : NotFoundComponent,
    meta: { layout: false }
   }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
