<template>
  <el-row type="flex" justify="center" align="center" >
    <el-col :span="12" :offset="6" class="grid-content">
      <h1>Login Form</h1>
      <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm" label-position="top">
        <el-form-item label="Username" prop="username">
          <el-input v-model="ruleForm.username" placeholder="Please input username" clearable></el-input>
        </el-form-item>
        <el-form-item label="Password" prop="password">
          <el-input type="password" v-model="ruleForm.password" autocomplete="off" placeholder="Please input password" show-password clearable></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">Login</el-button>
          <el-button @click="resetForm('ruleForm')">Reset</el-button>
        </el-form-item>
    
    </el-form>
    <el-button type="text" @click="()=>this.$router.push('/register')">Click here</el-button> to sign up!
    </el-col>
  </el-row>

</template>



<script>
import axios from 'axios';
import errorHandler from '../utils/errorHandling.js'
  export default {
    name : 'Login',
    data() {

      // Below 2 methods are used as a part of element ui form validation functionality
      // Here validation of username and password fields has been done before sending the request to backend
       let validateUsername = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please input the username'));
        }
         else {
              callback();
        }
      };
      let validatePassword = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please input the password'));
        }
        else {
              callback();
          } 
      };

      return {
        errors : [],
        ruleForm: {
          username:'',
          password: ''
        },
        // Part of element ui form validation
        rules: {
          username: [
            { required: true, validator: validateUsername, trigger: 'blur' }
          ],
          password: [
            { required : true, validator: validatePassword, trigger: 'blur' }
          ],
        }
      };
    },

     mounted(){
        if(this.$store.state.isAuthenticated){
            this.$router.push('/')
        }
        document.title = 'Login'
    },

    methods: {
      // For logging in the user
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
  
          if (valid) {
            localStorage.removeItem('token')
            const formData = {
              username : this.ruleForm.username,
              password : this.ruleForm.password
            }

            axios.post('/rest-auth/login/', formData)
            .then((response)=>{
              const auth_key = response.data.key;

              this.$store.commit('setToken', auth_key);
              axios.defaults.headers.common['Authorization'] = "Token "+ auth_key;
              localStorage.setItem('token', auth_key);

              const toPath = this.$route.query.to || '/';
              return this.$router.push(toPath);

            })
            .catch(error => {
                let vm = this
                errorHandler(error, vm)
            })
          } 
          else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      // For resetting the form
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>

<style>
  .grid-content{
    text-align:center;
  }
</style>
