<template>
    <div class="assess">
        <close-header></close-header>

        <div class="column">
            <div class='item h20'><q-button @click="$router.push('/')" theme="link"><h1>{{user.firstName+" "+user.lastName}}</h1></q-button></div>
            <div class='item h20'><qrcode-vue :value="user.qrcode" size="200" level="H" background="#edf1f4" foreground="#2c3e50"/></div>
            <span class="material-icons-outlined">qr_code</span>
        </div>

    </div>
</template>

<script>
import CloseHeader from './CloseHeader.vue'
import QrcodeVue from 'qrcode.vue'
import axios from 'axios'
export default {
  components: { CloseHeader, QrcodeVue },
    name: 'AssessUser',
    data() {
        return{
            score: 4,
            max: 5,
            min: 1,
            isCommenting: false,
            comment: '',
            user:{
                id: -1,
                firstName: '',
                lastName: '',
                email: '',
                qrcode: ""
            }
        }
    },
    mounted(){
        this.getUserInfos()
    },
    methods: {
        getUserInfos(){
            axios.get(this.$router.routeApi('/users/' + this.$route.params.id + '/'))
                .then(response => {
                    this.user.id = response.data.id
                    this.user.firstName = response.data.first_name
                    this.user.lastName = response.data.last_name
                    this.user.email = response.data.email
                    //this.user.qrcode = window.location.href;
                    console.log(this.user)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>
