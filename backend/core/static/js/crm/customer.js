const url = '/api/v1/crm/customer/';
const headers = {"Content-Type": "application/json"};

const getItems = () => ({
    filteredItems: [],
    editItem: {},

    init() {
        this.getData();
    },

    getData() {
        axios.get(url).then(response => {
            this.filteredItems = response.data;
        });
    },

    resetForm() {
        this.editItem = {};
    },

    saveData() {
        if (!this.editItem.id) { // Verifique se é uma edição ou adição
            axios.post(url, this.editItem, { headers: headers })
                .then(response => {
                    this.filteredItems = [response.data, ...this.filteredItems];
                    this.resetForm();
                });
        } else {
            axios.put(`${url}${this.editItem.id}/`, this.editItem, { headers: headers })
                .then(response => {
                    const index = this.filteredItems.findIndex(item => item.id === response.data.id);
                    this.filteredItems[index] = response.data;
                    this.resetForm();
                });
        }
    },

    editItemFn(item) {
        console.log("teste");
        this.editItem = { ...item }; // Copia os dados do item para o editItem
    },

    delete(item) {
        axios.delete(`${url}${item.id}/`, { headers: headers })
            .then(() => {
                this.filteredItems = this.filteredItems.filter(i => i.id !== item.id);
                this.resetForm();
            });
    },
});

