<template>

    <BookForm :key="book.id" :book="book" v-on:createBook="createBook" :update="false" :create="true" />

</template>


<script>
import axios from 'axios';
import BookForm from '../components/BookForm.vue';
import errorHandler from '../utils/errorHandling';
export default {
  name : 'CreateBook',
  
  components: { BookForm },
    data() {
      return {
        errors : [],
        book : {
          title : '',
          author : '',
          description : '',
          get_poster_image: ''
        }
      }
    },

    mounted(){
            document.title = "Create Book"
    },

    methods : {
      // For adding a new book
      async createBook(bookObj){
    
        await axios.post('/api/books/', bookObj)
        .then((response)=>{
            this.$message({
                      type:'success',
                      message :'You book has been added !'
                  })
             this.$router.push(`/`)
        })
        .catch((error)=>{
            let vm = this
            errorHandler(error, vm)
            })
          }

      }
    }
  
</script>

  
