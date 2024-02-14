// import { createRequire } from 'module';
// const require = createRequire(import.meta.url);

const mysql = require('mysql');

// 创建数据库连接
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '123456',
  database: 'sys' // 数据库名
});
// 连接到数据库
connection.connect((err) => {
  if (err) {
    console.error('连接数据库失败:', err);
    return;
  }
  console.log('成功连接到数据库');
  
  //执行查询操作
  var sql = "SELECT * FROM world";
  connection.query(sql, (err, rows) => {
    if (err) {
      console.error('查询失败:', err);
      return;
    }
    console.log('查询结果:', rows);

    var name_park = []; // 创建一个空数组来存储 name 字段值
    var lnglats = []; // 创建一个空数组来存储 lng 和 lat 字段值
    rows.forEach(row => {
      // 将每一行数据的 name 字段值传递给指定的变量
      var name = row.name;
      var lng =row.lng;
      var lat =row.lat;
      

      name_park.push(name);
      lnglats.push([lng, lat]);
      
      // console.log('公园名称:', name);
      // console.log(name+'lng', lng);
      // console.log(name+'lat', lat);
      
    });
    console.log(name_park);
    console.log(lnglats);


    // 关闭数据库连接
    connection.end();
    console.log('关闭数据库连接')
  });
});



