<template>
    <div class="container">
        <el-row :gutter="20" v-if="books.length>0">
            <BookCard v-for="book in books" :key="book.id" :book="book" v-on:deleteBook="deleteBook" />
        </el-row>
        <el-row :gutter="20" v-else>
           <h2>Oops ! No favourite books available.You can add books by clicking on add book link at the top.</h2>
        </el-row>
    </div>
</template>


<script>

import BookCard from '../components/BookCard.vue'
import axios from 'axios';
import errorHandler from '../utils/errorHandling.js'

export default {

    name : "Home",

    components : {
        BookCard
    },

    data(){
        return {
            books : []
        }
    },

    mounted(){
        this.getBooks()
        document.title = 'HomePage'
    },

    methods:{
        //  For fetching all books which belongs to currently logged in user
        async getBooks(){
            this.$store.commit('setIsLoading', true)
            await axios.get('/api/books/').then((response)=>{
                this.books = response.data
            })
            .catch(error => {
                let vm =this
                errorHandler(error, vm)
            })
            
            this.$store.commit('setIsLoading', false)

        },

        // Deleting a book which is sent from child component 'BookCard'
        async deleteBook(book){
            this.$store.commit('setIsLoading', true)
            await axios.delete(`/api/book/${book}/`).then((response)=>{
                 this.$message({
                    message: 'Book has been deleted',
                    type: 'success'
                });
                this.books = this.books.filter(bookObj => bookObj.id != book);
            })
            .catch(error => {
                this.$store.commit('setIsLoading', false)
                errorHandler(error, vm=this)
               
            })
            
            this.$store.commit('setIsLoading', false)

        },

    }
}


</script>


<style>
.container {
    margin-left: auto;
    margin-right : auto;
    padding : 20px;
    
}
</style>
