<script>
    import { currentStep, tripDetails } from '../stores';
    import { onMount } from 'svelte';
  
    let origin = '';
  
    function selectOrigin(city) {
      origin = city;
    }
  
    function addInfoOrigin() {
      tripDetails.update(details => ({ ...details, origin }));
      currentStep.set(2);
    }
  
    function goToStep(step) {
      currentStep.set(step);
    }
  </script>
  
  <div class="step">
    <div class="grey-rect">
      <div class="desc-img">
        <p class="dir-desc">Откуда</p>
        <img src="images/location-pin-alt-svgrepo-com.svg" class="dir-image">
      </div>
      <div class="but-text">
        <div class="buttons">
          <button class="button1" id="left1" on:click={() => selectOrigin('Иннополис')}>Иннополис</button>
          <button class="button1" id="right1" on:click={() => selectOrigin('Казань')}>Казань</button>
        </div>
        <textarea id="comment1" class="com" placeholder="Уточните место отправления..." bind:value={origin}></textarea>
      </div>
      <div class="nav-buttons">
        <button class="next" id="dir-button1" on:click={() => goToStep(0)}>Назад</button>
        <button class="next" id="dir-button2" on:click={addInfoOrigin}>Далее</button>
      </div>
    </div>
  </div>
  
  <style>

  </style>
  