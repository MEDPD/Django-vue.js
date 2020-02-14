axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
class Form{
    constructor(data){
        this.trueData = data
        for(let field in data)
           this[field] = data[field]
    }
    data(){
        let data = new FormData()
        for(let field in this.trueData)
           data.append(field, this[field])
        return data
    }
    reset(){
        for(let field in this.trueData)
            this[field] = ''
    }
    post(url){

        return new Promise((resolve, reject) => {
            axios.post(url, this.data()).then(
                  res => { 
                      this.success()
                      resolve(res)
                })
            .catch(
                err => {
                    reject(err)
                }
            )
        });
    }
    success(){
        console.log("success")
        this.reset()
    }
}
new Vue({
    delimiters: ['[[', ']]'],
    el: '#root',
    data:{
        form : new Form({
            todo_i:'',
            prop:''
        }),
        todos: []
    },
    mounted() {
        axios.get('todos').then(res => {
            this.todos = JSON.parse(res.data)
            
            // console.log(JSON.parse(res.data))

        }).catch(err => console.log("err1:" + err))
    },
    methods:{
        onSubmit(){
            this.form.post('add').then(res => this.todos = JSON.parse(res.data)).catch(
                err => console.log(err)
            )

        },
        deleteTodo(pk){
            axios.get('delete',{
                params: {
                  id: pk 
                }
            }).then(res => this.todos = JSON.parse(res.data))
            .catch(err => console.log("err3:" + err))
        }
    }
})