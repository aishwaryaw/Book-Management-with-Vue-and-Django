<template >
 
    <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="4" class="container">
      <el-card :body-style="{ padding: '0px', width:'100%'}">
        <img v-bind:src="book.get_poster_image" v-if="book.get_poster_image" class="image"/>
        <img class="image" src="https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg" v-else />
        <div style="padding: 14px;">
          <div><h2>Book title : {{book.title}}</h2></div>
          <div><h5><i>Book author : {{book.author}}</i></h5></div>
          <div class="bottom clearfix">
            <el-row>
              <el-tooltip class="item" effect="dark" content="View description of book" placement="bottom"><el-button type="info" icon="el-icon-info" @click="dialogVisible = true" round>Description</el-button></el-tooltip>
              <el-tooltip class="item" effect="dark" content="Edit book" placement="bottom"><el-button type="primary" icon="el-icon-edit" @click="()=>$router.push(`/book/edit/${book.id}`)" round></el-button></el-tooltip>
              <el-tooltip class="item" effect="dark" content="Delete a book" placement="bottom"><el-button type="danger" icon="el-icon-delete" @click="deletedialogVisible=true" round></el-button></el-tooltip>
            </el-row>
          </div>
        </div>
      </el-card>
      <el-dialog
          title="Book description"
          :visible.sync="dialogVisible"
          width="30%">
          <span>{{book.description || 'No description available'}}</span>
          <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">Cancel</el-button>
          </span>
      </el-dialog>

      <el-dialog
        title="Delete Book"
        :visible.sync="deletedialogVisible"
        width="30%" center>
        <span>Are you sure you want to delete the book ?</span>
        <span slot="footer" class="dialog-footer">
          <el-button @click="deletedialogVisible = false">Cancel</el-button>
          <el-button type="primary" @click="deleteBook(book.id)">Confirm</el-button>
        </span>
      </el-dialog>
    </el-col>

</template>

<script>
export default {
  name : 'BookCard',
  props : {
    book : Object
  },
  data(){
    return{
      dialogVisible : false,
      deletedialogVisible : false
    }
  },

  methods : {
    // Delete book event will be emitted here which we will be catched in parent Home component
    deleteBook(book){
      this.deletedialogVisible = false
      this.$emit('deleteBook', book)
    }
  }
}


</script>


<style>

.container{
  text-align : center;
}
 .image {
    height:200px;
    width:100px;
    width: 100%;
    display: block;
  }


</style>
