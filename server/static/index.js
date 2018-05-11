var socket = io.connect('http://' + document.domain + ':' + location.port);

var visualEl = document.getElementById('visual');
var level1El = document.getElementById('visual-1');
var level2El = document.getElementById('visual-2');
var level3El = document.getElementById('visual-3');
var level4El = document.getElementById('visual-4');

socket.on('connect', function() {
  socket.emit('my event', {data: 'I\'m connected!'});
});

socket.on('my update', function(data) {

  console.log('UPDATE FROM SERVER YAY!');

  if (data['water-level']) {
    // TODO we can refactor this to reduce duplication later
    switch (data['water-level']) {
      case 0:
        visualEl.classList.add('empty');
        break;
      case 1:
        visualEl.classList.remove('empty');
        level1El.classList.add('show');
        level2El.classList.remove('show');
        level3El.classList.remove('show');
        level4El.classList.remove('show');
        break;
      case 2:
        visualEl.classList.remove('empty');
        level1El.classList.add('show');
        level2El.classList.add('show');
        level3El.classList.remove('show');
        level4El.classList.remove('show');
        break;
      case 3:
        visualEl.classList.remove('empty');
        level1El.classList.add('show');
        level2El.classList.add('show');
        level3El.classList.add('show');
        level4El.classList.remove('show');
        break;
      case 4:
        visualEl.classList.remove('empty');
        level1El.classList.add('show');
        level2El.classList.add('show');
        level3El.classList.add('show');
        level4El.classList.add('show');
        break;
    }
  }
});