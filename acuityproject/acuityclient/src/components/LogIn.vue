<template>
    <div class="log-in">
        <h1>Acuity</h1>
        <h3>Log in</h3>
        <q-form ref="form" :rules="rules">
            <q-form-item label="Username" prop="username">
                <q-input v-model="username" type="text"/>
            </q-form-item>
            <q-form-item label="Password" prop="password">
                <q-input v-model="password" type="password"/>
            </q-form-item>
            
            <p v-if="isLoading"><q-button loading>Log in</q-button></p>
            <p v-else><q-button @click="submitForm">Log in</q-button></p>
        </q-form>
    </div>
</template>

<script>

import axios from 'axios'
export default {
    name: 'LogIn',

    data() {
        return{
            username: '',
            password: '',

            isLoading: false,

            rules: {
                username: [
                    { required: true }
                ],
                password: {
                    required: true
                }
            },
        }
    },
    methods: {
        submitForm(){
            this.isLoading = true;

            const formData = {
                username: this.username,
                password: this.password,
            }

            axios.post('http://localhost:8000/api/token/login', formData)
                .then(response => {
                    console.log(response)
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization'] = "Token " + token

                    localStorage.setItem("token", token)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
}
</script>
