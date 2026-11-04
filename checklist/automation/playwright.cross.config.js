const{defineConfig}=require('@playwright/test');const path=require('path');
module.exports=defineConfig({testDir:__dirname,workers:1,retries:0,timeout:120000,
 reporter:[['line'],['json',{outputFile:path.resolve(process.env.CROSS_PW_JSON||path.join(__dirname,'cross-platform/playwright-results.json'))}]],
 outputDir:path.resolve(process.env.CROSS_OUTPUT || path.join(__dirname,'cross-platform/test-results')),
 use:{baseURL:'http://localhost:5173',actionTimeout:10000,navigationTimeout:20000,screenshot:'off',trace:'off'},
 projects:[{name:'firefox',testMatch:'run-firefox.spec.js',use:{browserName:'firefox',viewport:{width:1280,height:800}}},{name:'androidchrome',testMatch:'run-androidchrome.spec.js',use:{browserName:'chromium',viewport:null}}]
});
