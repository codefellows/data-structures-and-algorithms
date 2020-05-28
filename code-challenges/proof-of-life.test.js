'use strict';

function isAlive() {
  return true;
}


describe('proof of life', () => {

  it('lives', () => {

    expect(isAlive()).toBeTruthy();

  });

});

