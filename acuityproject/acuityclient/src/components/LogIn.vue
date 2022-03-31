<template>
    <div class="h100">
        <main-header></main-header>
        <div class="log-in">

            <!-- <h1>Acuity</h1> -->
            <h3>Log in</h3>
            <q-form ref="form" :rules="rules" showErrorMessage>
                <q-form-item label="Email" prop="email">
                    <q-input v-model="email" type="text"/>
                </q-form-item>
                <q-form-item label="Password" prop="password">
                    <q-input v-model="password" type="password"/>
                </q-form-item>
                <q-form-item :label="error"></q-form-item>
                <q-button @click="submitForm">Log in</q-button>
            </q-form>
        </div>
    </div>
</template>

<script>

import axios from 'axios'
import MainHeader from './MainHeader.vue'
export default {
  components: { MainHeader },
    name: 'LogIn',

    data() {
        return{
            email: '',
            password: '',
            error: '',
            isLoading: false,

            rules: {
                email: [
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
                password: this.password,
                email: this.email
            }

            axios.post('http://localhost:8000/api/token/login', formData)
                .then(response => {
                    console.log(response)
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization'] = "Token " + token

                    localStorage.setItem("token", token)

                    this.$router.push("/")
                })
                .catch(error => {
                    if (error.response.status == 400){
                        this.error = "Wrong credentials"
                    }
                })
        }
    },
}
</script>
