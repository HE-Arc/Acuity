<template>
    <div class="assess">
        <close-header></close-header>

        <div class="column">
            <div class='item h20'><q-button @click="$router.push('/')" theme="link"><h1>{{user.firstName+" "+user.lastName}}</h1></q-button></div>
            
            <template v-if="!isCommenting">
                <div class="item h20"><q-button @click="updateScore(1)" :disabled="score >= max" class="assess-control" theme="secondary" type="icon" icon="q-icon-triangle-up" circle></q-button></div>
                <div class="item h20 assess-counter">{{score}}</div>
                <div class="item h20"><q-button @click="updateScore(-1)" :disabled="score <= min" class="assess-control" theme="secondary" type="icon" icon="q-icon-triangle-down" circle></q-button></div>
            
                <div class="item h20"><q-button class='assess-send' @click="isCommenting=true">Continue</q-button></div>
            </template>

            <template v-else>
                <div class="item h60">
                    <div class="q-form-item w80">
                        <div class="q-form-item__header">
                            <label for="email" class="q-form-item__label">Email</label>
                        </div>
                        <textarea v-model="comment" placeholder="Comment you judgement..."></textarea>
                    </div>                    
                </div>
                <div class="item h20"><q-button class='assess-send' @click="send">Send</q-button></div>
            </template>
        </div>

    </div>
</template>

<script>
import CloseHeader from './CloseHeader.vue'
import axios from 'axios'
export default {
  components: { CloseHeader },
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
                email: ''
            }
        }
    },
    mounted(){
        this.getUserInfos()
    },
    methods: {
        getUserInfos(){
            axios.get('http://localhost:8000/api/users/' + this.$route.params.id + '/')
                .then(response => {
                    this.user.id = response.data.id
                    this.user.firstName = response.data.first_name
                    this.user.lastName = response.data.last_name
                    this.user.email = response.data.email

                    console.log(this.user.email)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        updateScore(n){
            this.score += n;
            if(this.score > this.max)
                this.score = this.max
            else if(this.score < this.min)
                this.score = this.min
        },
        send(){
            const data = {
                score: this.score,
                toUser: this.$route.params.id,
                comment: this.comment,
            }

            console.log(axios.defaults.headers)

            axios.post('http://localhost:8000/api/assess/', data)
                .then(response => {
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
        },
    },
}
</script>
