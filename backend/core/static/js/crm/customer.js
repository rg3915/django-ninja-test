const url = '/api/v1/crm/customer/'
const headers = {"Content-Type": "application/json"}

const getItems = () => ({
    filteredItems: [],
    editItem: {},

    init(){
        this.getData()
    },

    getData(){
        axios.get(url).then(response => { this.filteredItems = response.data })
    },

    resetForm(){ //limpar o campo
        this.editItem={}
    },

    saveData(){
        if (!this.editItem){
            return
        }
        const bodyData = { ...this.editItem} //spread operator 
        axios.post(url, bodyData, {headers: headers})
            .then(response => console.log(response.data))
    },
})