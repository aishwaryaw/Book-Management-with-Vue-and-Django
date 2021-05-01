//  This method is used as an utility function by eachh component in order to handle errors 
// happening when request is sent to backend

const errorHandler = (error, vm) => {
    let errors = []
    if(error.message == "Request failed with status code 401"){
        errors.push('Something went wrong. Please try again')
        vm.$message({
            message: 'Oops! You are not logged in. Please login',
            type: 'error'
        });
        vm.$router.push('/login')
    }
    else if(error.response) {
        if(error.response.status == '404'){
            vm.$message({
                type:'error',
                message : error.response.data.message
            })
            vm.$router.push('/')
        }

        else{
            for(const property in error.response.data) {
                if(property == 'non_field_errors'){
                errors.push(error.response.data[property][0])
                }
                else{
                    errors.push(property.toUpperCase() + ':' + error.response.data[property][0]) 
                }
            }
                
                vm.$message({
                    type:'error',
                    message : errors[0]
                })
        }
            
    }
    else {
            errors.push('Something went wrong. Please try again')
            vm.$message({
                message: 'Oops! Some error occurred. Please try again after somme time',
                type: 'error'
            });
            // console.log(JSON.stringify(error))

        }
}

export default errorHandler
