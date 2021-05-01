<template>
    <div>

    <el-menu v-if="layout"
      class="el-menu-demo"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      >
      <template v-if="$store.state.isAuthenticated">
        <el-row :gutter="10" type="flex">
          <el-col :xs="12" :sm="6" :md="18" :lg="8" :xl="20" align="center"><div><el-menu-item><router-link class="linkColor" to="/">Home</router-link></el-menu-item></div></el-col>
            <el-col :xs="12" :sm="6" :md="18" :lg="8" :xl="20" align="center"><el-menu-item><el-link icon="el-icon-circle-plus-outline"><router-link to="/create/book" class="linkColor">Add a book</router-link></el-link></el-menu-item></el-col>
          <el-col :xs="12" :sm="6" :md="6" :lg="8" :xl="4" align="center"><div><el-menu-item><el-link type="success" icon="el-icon-lock" @click="logout()">Logout</el-link></el-menu-item></div></el-col>
        </el-row>
      </template>

      <template v-else>
      <el-row :gutter="10" type="flex" justify="end">
        <el-col :xs="8" :sm="12" :md="14" :lg="16" :xl="18" align="center"><div class="grid-content bg-purple"></div></el-col>
        <el-col :xs="8" :sm="6" :md="5" :lg="4" :xl="3" align="center"><el-menu-item><router-link class="linkColor" to="/login">Login</router-link></el-menu-item></el-col>
        <el-col :xs="8" :sm="6" :md="5" :lg="4" :xl="3" align="center"><el-menu-item><router-link class="linkColor" to="/register">Register</router-link></el-menu-item></el-col>
        </el-row>
      </template>

    </el-menu>

    <div class="section"
      v-loading="$store.state.isLoading"
      element-loading-text="Loading..."
      element-loading-spinner="el-icon-loading"
      element-loading-background="rgba(0, 0, 0)"
      style="width: 100%;">
      <router-view/>
    </div>

  </div>
</template>


<script>
import axios from 'axios';
  export default {
    data() {
      return {
        layout : this.$route.meta.layout
      }
    },
    
    beforeCreate(){
      // Vuex store initialization
      this.$store.commit('initializeStore')
      const token = this.$store.state.token;
      if(token){
        axios.defaults.headers.common['Authorization'] = `Token ${token}`
      }
      else{
        axios.defaults.headers.common['Authorization'] = ''
      }
    },

    mounted(){
      // if user is not authenticated and try to access any authorized route then he/she will redirected to login page
        if(!this.$store.state.isAuthenticated){
            this.$router.push('/login')
        }
        
    },


    methods :{
      // Logging out the current user
      logout(){
        this.$store.commit('removeToken')
        axios.defaults.headers.common['Authorization'] = ""
        localStorage.removeItem('token')
        this.$router.push('/login')
      }
    }

    }
</script>


<style>
.linkColor{
  color : #fff;
  text-decoration:none
}



</style>
