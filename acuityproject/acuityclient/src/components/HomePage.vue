<template>
    <div class="home-page">
        <h1>Acuity</h1>
        <h3>Homepage</h3>
    </div>
</template>


<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                // Users
                usersList: [''],
            }
        },
        methods: {
            async getData() {
                try {
                    axios.get('http://localhost:8000/api/home-page/')
                        .then(response => this.usersList = response.data);
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
            async submitForm(){
                try {
                    // Send a POST request to the API
                    axios.post('http://localhost:8000/api/tasks/', {
                        title: this.title,
                        description: this.description,
                        completed: false
                    }).then(response => this.tasks.push(response.data));
                    // Reset the title and description field values.
                    this.title = '';
                    this.description = '';
                } catch (error) {
                    // Log the error
                    console.log(error);
                }
            },
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>
