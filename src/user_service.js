// 用户服务，用于演示 WorkBuddy 自动巡检。

const db = require('./db');

// BUG: return 写在 .then 回调里，外层 async 函数实际返回 undefined
async function getUser(id) {
  db.findUser(id).then((user) => {
    return user;
  });
}

// BUG: 缺少 try/catch，db.findAll() 抛错时直接冒泡；且 active 字段未做空值判断
async function listActiveUsers() {
  const users = db.findAll();
  return users.filter((u) => u.active);
}

module.exports = { getUser, listActiveUsers };
