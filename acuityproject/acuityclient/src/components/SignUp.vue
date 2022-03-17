<template>
    <div class="log-in">
        <h1>Acuity</h1>
        <h3>Sign up</h3>
        <q-form ref="form" :rules="rules">
            <q-form-item label="First name" prop="firstName">
                <q-input v-model="firstName" type="text"/>
            </q-form-item>
            <q-form-item label="Last name" prop="lastName">
                <q-input v-model="lastName" type="text"/>
            </q-form-item>
            <q-form-item label="E-mail" prop="email">
                <q-input v-model="email" type="email"/>
            </q-form-item>
            <q-form-item label="Password" prop="password">
                <q-input v-model="password" type="password"/>
            </q-form-item>
            
            <p v-if="isLoading"><q-button loading>Sign up</q-button></p>
            <p v-else><q-button @click="submitForm">Sign up</q-button></p>
        </q-form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'SignUp',
    data() {
        return{
            lastName: '',
            firstName: '',
            password: '',
            email: '',

            isLoading: false,

            rules: {
                lastName: { 
                    required: true
                },
                firstName: { 
                    required: true
                },
                password: {
                    required: true
                },
                email: {
                    required: true,
                },
            },
        }
    },
    methods: {
        submitForm(){
            const formData = {
                last_name: this.lastName,
                first_name: this.firstName,
                email: this.email,
                password: this.password,
            }

            axios.post('http://localhost:8000/api/users/', formData)
                .then(response => {
                    this.$router.push('/log-in')
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
}
</script>
