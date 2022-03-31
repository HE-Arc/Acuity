<template>
    <div class="assess">
        <close-header></close-header>

        <div class="column">

            <div class='item h20'><q-button @click="$router.push('/users/'+user.id)" theme="link"><h1>{{user.firstName+" "+user.lastName}}</h1></q-button></div>
            
            <template v-if="!isCommenting">
                <div class="item h20"><q-button @click="updateScore(1)" :disabled="assess.score >= max" class="assess-control" theme="secondary" type="icon" icon="q-icon-triangle-up" circle></q-button></div>
                <div class="item h20 assess-counter">{{assess.score}}</div>
                <div class="item h20"><q-button @click="updateScore(-1)" :disabled="assess.score <= min" class="assess-control" theme="secondary" type="icon" icon="q-icon-triangle-down" circle></q-button></div>
            
                <div class="item h20"><q-button class='assess-send' @click="isCommenting=true">Continue</q-button></div>
            </template>

            <template v-else>
                <div class="item h60">
                    <div class="q-form-item w80">
                        <div class="q-form-item__header">
                            <label for="email" class="q-form-item__label">Email</label>
                        </div>
                        <textarea class="custom-qui" v-model="assess.comment" placeholder="Comment you judgement..."></textarea>
                    </div>                    
                </div>
                <div class="item h20"><q-button class='assess-send' @click="send">Send</q-button></div>
            </template>
        </div>
    </div>
</template>

<script>
import CloseHeader from './CloseHeader.vue'
//import QrcodeVue from 'qrcode.vue'
import axios from 'axios'
export default {
  components: { CloseHeader },
    name: 'AssessUser',
    data() {
        return{
            max: 5,
            min: 1,
            isCommenting: false,
            
            user:{
                id: -1,
                firstName: '',
                lastName: '',
                email: ''
            },
            assess:{
                score: 4,
                comment: ''
            }
        }
    },
    mounted(){
        this.getExistentAssess()
    },
    created(){
        this.user.qrcode = window.location.href;
    },
    methods: {
        getExistentAssess(){
            axios.get('http://localhost:8000/api/assess/4/myAssessOf/')
                .then(response=>{
                    if(response.status == 204)
                        this.getUserInfos()
                    else{
                        this.fillUser(response.data.toUser)
                        this.fillAssess(response.data)
                    }   
                })
                .catch(error=>{
                    console.log(error)
                })
        },
        getUserInfos(){
            axios.get('http://localhost:8000/api/users/' + this.$route.params.id + '/')
                .then(response => {
                    this.fillUser(response.data)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        fillUser(data){
            this.user.id = data.id
            this.user.firstName = data.first_name
            this.user.lastName = data.last_name
            this.user.email = data.email
        },
        fillAssess(data){
            this.assess.comment = data.comment
            this.assess.score = data.score
        }
        ,
        updateScore(n){
            this.assess.score += n;
            if(this.assess.score > this.max)
                this.assess.score = this.max
            else if(this.assess.score < this.min)
                this.assess.score = this.min
        },
        send(){
            const data = {
                score: this.assess.score,
                toUser: this.$route.params.id,
                comment: this.assess.comment,
            }

            axios.post('http://localhost:8000/api/assess/', data)
                .then(()=>{
                    this.$router.push('/users/'+this.user.id)
                })
                .catch(error => {
                    console.log(error)
                })
        },
    }
}
</script>
