<template>

    <BookForm :key="book.id" :book="book" v-on:updateBook="updateBook" :update="true" :create="false" />

</template>



<script>

import axios from 'axios';
import BookForm from '../components/BookForm.vue';
import errorHandler from '../utils/errorHandling';
export default {
    name : 'EditBook',

    components: { BookForm },

    data() {
        return {
            errors : [],
            book : {},
            bookId : this.$route.params.bookId
        }
        },

    mounted(){
            this.getBook()
            document.title = "Edit Book"
        },

    methods : {

        // Fetching the given book details from backend depending on ID provided, 
        // This method is used for pre-populating the book details in update form
        async getBook(){
            this.$store.commit('setIsLoading', true)
            await axios.get(`/api/book/${this.bookId}/`)
            .then((response)=>{
                this.book = response.data
            })
            .catch(error => {
                let vm = this
                errorHandler(error, vm)
                })
                
            this.$store.commit('setIsLoading', false)

            },

        // This method is used for updating the given book details
        async updateBook(bookObj){

            await axios.put(`/api/book/${this.bookId}/`, bookObj)
            .then((response)=>{
                this.$message({
                        type:'success',
                        message :'Your book details has been updated !'
                    })
                this.$router.push('/')
            })
            .catch((error)=>{
                this.$store.commit('isLoading', true)
                let vm = this
                console.log(errorHandler(error,vm))
                this.$store.commit('isLoading', false)
            })

        }
    }
}
  
</script>

  
