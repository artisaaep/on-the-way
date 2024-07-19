<script>
    import { currentStep, tripDetails } from '../stores';
  
    function selectRole(role) {
      tripDetails.update(details => ({ ...details, role }));
      currentStep.set(1);
    }
  </script>
  
  <div class="step active">
    <div class="pdiv">
      <p class="q">В какой роли вы хотели бы</p>
      <p class="q">совершить поездку?</p>
    </div>
    <div id="buttonschoose">
      <button id="btnc" on:click={() => selectRole('driver')}>
        <p class="buttonchoose">Водитель</p>
      </button>
      <button id="btnc" on:click={() => selectRole('passenger')}>
        <p class="buttonchoose">Пассажир</p>
      </button>
    </div>
    <div class="img-cont">
      <img src="images/car-svgrepo-com.svg">
    </div>
  </div>
  
  <style>
    
  </style>
  