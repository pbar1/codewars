function solve(arr){
  const forwards = arr.map(findForward);
  const backwards = arr.map(findBackward);

  const foo = arr.map(n => checkExists(n, forwards));
  const bar = arr.map(n => checkExists(n, backwards));

  console.log(foo);
  console.log(bar);
}

function findForward(n) {
  let ns = [];
  if (n % 3 === 0) ns.push(n / 3);
  ns.push(n * 2);
  return ns;
}

function findBackward(n) {
  let ns = [];
  ns.push(n * 3);
  if (n % 2 === 0) ns.push(n / 2);
  return ns;
}

function checkExists(n, ns) {
  return ns.indexOf(n) < 0;
}

solve([12,3,9,4,6,8]);
