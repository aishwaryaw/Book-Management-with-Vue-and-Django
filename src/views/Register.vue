<template>
  <el-row type="flex" justify="center" align="center">

    <el-col :span="12" :offset="6" class="grid-content">
      <h1>Signup Form</h1>
      <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm" label-position="top">
        <el-form-item label="Username" prop="username">
          <el-input v-model="ruleForm.username" placeholder="Please input username" clearable></el-input>
        </el-form-item>
        <el-form-item label="Password" prop="password">
          <el-input type="password" v-model="ruleForm.password" autocomplete="off" placeholder="Please input password" show-password clearable></el-input>
        </el-form-item>
        <el-form-item label="Confirm Password" prop="checkPassword">
          <el-input type="password" v-model="ruleForm.checkPassword" autocomplete="off" placeholder="Please input password again" show-password clearable></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">Register</el-button>
          <el-button @click="resetForm('ruleForm')">Reset</el-button>
        </el-form-item>
      
      </el-form>
      <el-button type="text" @click="()=>this.$router.push('/login')">Click here</el-button> to login!
    
    </el-col>

  </el-row>

</template>



<script>
import axios from 'axios';
import errorHandler from '../utils/errorHandling.js';
  export default {
    name : 'Register',
    data() {

      // Below 3 methods are used as a part of element ui form validation functionality
      // Here validation of username and password fields has been done before sending the request to backend

       var validateUsername = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please input the username'));
        } else {
          callback();
        }
      };
      var validatePassword = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please input the password'));
        } else {
          if (this.ruleForm.checkPassword !== '') {
            this.$refs.ruleForm.validateField('checkPassword');
          }
          callback();
        }
      };
      var validateConfirmPassword = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please input the password again'));
        } else if (value !== this.ruleForm.password) {
          callback(new Error('Two inputs don\'t match!'));
        } else {
          callback();
        }
      };

      return {
        errors : [],
        ruleForm: {
          username:'',
          password: '',
          checkPassword: '',
        },
        rules: {
          username: [
            { required: true,validator: validateUsername, trigger: 'blur' }
          ],
          password: [
            { required : true, validator: validatePassword, trigger: 'blur' }
          ],
          checkPassword: [
            {required:true, validator: validateConfirmPassword, trigger: 'blur' }
          ],
        }
      };
    },

    mounted(){
        if(this.$store.state.isAuthenticated){
            this.$router.push('/')
        }
        document.title = 'Register'
    },

    methods: {
      // Performing registration of user
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            const formData = {
              username : this.ruleForm.username,
              password1 : this.ruleForm.password,
              password2 : this.ruleForm.checkPassword
            }

            axios.post('/rest-auth/registration/', formData).then((response) =>{
               this.$message({
                message: 'Congrats! Your account has been created, You can login now',
                type: 'success'
            });

              this.$router.push('/login')
            })
            .catch(error => {
              let vm = this;
              errorHandler(error, vm)
    
            });
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
