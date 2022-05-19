<template>
  <div class="home">
      <ConnectScreen/>
  </div>
</template>

<script lang="ts">
import { Options, Vue} from 'vue-class-component';
import ConnectScreen from '@/components/ConnectScreen.vue'; // @ is an alias to /src  

@Options({
  components: {
    ConnectScreen,
  },
})
export default class HomeView extends Vue {}
</script>
