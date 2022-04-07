<template>
    <div class="h100">
        <div class="log-in">
            <h1><img class="mini-logo block__content" src="../assets/Vector.svg">Acuity</h1>
            <h3>Log in</h3>
                <q-form ref="form" :model="model" :rules="rules">
                    <q-form-item label="Email" prop="email">
                        <q-input v-model="model.email" type="text"/>
                    </q-form-item>
                    <q-form-item label="Password" prop="password">
                        <q-input v-model="model.password" type="password"/>
                    </q-form-item>
                    
                    <p v-if="isLoading"><q-button loading>Log in</q-button></p>
                    <p v-else><q-button @click="submitForm">Log in</q-button></p>
                </q-form>
        </div>
    </div>
</template>

<script>

import axios from 'axios'
export default {
  components: { },
    name: 'LogIn',

    data() {
        return{
            error: '',
            model:{
                email: '',
                password: '',
            },
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
                password: this.model.password,
                email: this.model.email
            }
            console.log(formData)
            axios.post(this.$router.routeApi('/token/login'), formData)
                .then(response => {
                    console.log(response)
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization'] = "Token " + token

                    localStorage.setItem("token", token)

                    this.$router.push('/')
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
