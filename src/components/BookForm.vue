<template>
  <el-row type="flex" justify="center" align="center">

    <el-col :span="12" :offset="6" class="grid-content">
      <h1>Book Form</h1>
      <el-form status-icon label-width="120px" label-position="top">
        
        <el-form-item label="Book title" >
          <el-input v-model="book.title" placeholder="Please input book title" v-on:input="handleChange" clearable></el-input>
        </el-form-item>

        <el-form-item label="Book author name" >
          <el-input v-model="book.author" placeholder="Please input book author" v-on:input="handleChange" clearable></el-input>
        </el-form-item>

        <el-form-item label="Book description" >
          <el-input type="textarea" :rows="2" v-model="book.description" v-on:input="handleChange" placeholder="Please input descritption" clearable></el-input>
        </el-form-item>

        <el-form-item>
          <el-upload v-if="fileList[0].url != ''"
            action="https://book-management-vue-django.herokuapp.com/api/book_image/"
            list-type="picture-card"
            :on-preview="handlePictureCardPreview"
            :limit="1"
            :on-remove="handleRemove"
            :on-success="handleSuccess"
            :before-upload="handleBeforeUpload"
            :file-list="fileList"
            >
            <i class="el-icon-plus"></i>
            </el-upload>

         <el-upload v-else
            action="https://book-management-vue-django.herokuapp.com/api/book_image/"
            list-type="picture-card"
            :on-preview="handlePictureCardPreview"
            :limit="1"
            :on-remove="handleRemove"
            :on-success="handleSuccess"
            :before-upload="handleBeforeUpload"
            >
            <i class="el-icon-plus"></i>
            </el-upload>

            <el-dialog :visible.sync="dialogVisible">
            <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>

        </el-form-item>

        <el-form-item>        
          <el-button v-if="create" type="primary" @click="submitForm(book)">Add a book</el-button>
           <el-button v-else-if="update" type="primary" :disabled="!changed" @click="submitForm(book)">Update a book</el-button>
          <el-button @click="resetForm()">Reset</el-button>
        </el-form-item>
      
      </el-form>

    </el-col>

  </el-row>

</template>



<script>

export default {
    name : 'BookForm',

    props : {
        book : Object,
        create : Boolean,
        update : Boolean
    },
    data() {
      return {
        book : this.book,
        create: this.create,
        update : this.update,
        changed : false,
        dialogImageUrl: '',
        dialogVisible: false,
        poster_image  : this.book.get_poster_image,
        fileList : [{
          url : this.book.get_poster_image,
        }],
      }
    },
    methods: {
      // Below 4 methods are used as a part of element ui upload component for image handling
      // 1. This method will run after the uploaded image file has been deleted
      handleRemove(file) {
        this.changed= true;
        this.poster_image = ''
      },
      // 2. This menthod will run when user clicks on image for viewing it
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },

      // 3. This method will run  just before file upload
      handleBeforeUpload(file) {
        const isImage = file.type === 'image/jpeg' || file.type === 'image/png';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isImage) {
          this.$message.error('Book picture must be JPG/PNG format!');
        }
        if (!isLt2M) {
          this.$message.error('Book picture size can not exceed 2MB!');
        }
        return isImage && isLt2M;
      },

      // 4. This method will run after the image file has been uploaded successfully.
      handleSuccess(res,file){
          this.changed= true;
          function toDataURL(url, callback) {
          var xhr = new XMLHttpRequest();
          xhr.onload = function() {
            var reader = new FileReader();
            reader.onloadend = function() {
              callback(reader.result);
            }
            reader.readAsDataURL(xhr.response);
          };
          xhr.open('GET', url);
          xhr.responseType = 'blob';
          xhr.send();
        }
        let vm = this;
        toDataURL(URL.createObjectURL(file.raw), function(dataUrl) {
          vm.poster_image = dataUrl;
          
        })
      },

      // Below method is used when above form is used for updating the existing book details instead of creating a new book.
      // Update book method will be enabled only if any particular field is changed
      handleChange(evt){
        this.changed= true
      },

      // Submitting the form
      submitForm(book) {
        const bookObj = {
                title : book.title,
                author: book.author,
                description : book.description
        }

        if(this.poster_image != '') {
          bookObj.poster_image = this.poster_image
        }

          if(this.create){
            this.$emit('createBook', bookObj)
          }
          else{
            this.$emit('updateBook', bookObj)
          }
        },

      //  For resetting the filled form
        resetForm(){
          this.book.title = '';
          this.book.author = '';
          this.book.description = '';
          this.fileList[0].url = '';
          this.poster_image = '';
        }
       
      }   
  }

</script>


<style>
  .grid-content{
    margin-left : 20px;
  }
</style>
  
