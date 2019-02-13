// alert("Welcome to Unit Converter")
// while (true) {
    // var convert_to_meters = {"feet in meter": 3.2804, "ft": .3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": .9144, "in": .0254, "cm": .01, "mm": .001};
//     while (true) {
//         try {
//             var input_number = prompt("Let's do some unit of measurement conversions. Please enter the number of units you wish to convert.");
//             break;
//         except ValueError {
//             alert("Please enter a number.");
//         }
//     }
//     var input_unit = prompt("What unit of measurement do you wish to convert? > ");
//     var output_unit = prompt("What unit of measurement do you wish to convert to? > ");
//     var meters = parseFloat(input_number * convert_to_meters[input_unit]);
//     var output_number = parseFloat(meters / convert_to_meters[output_unit]);
//     print(f"Your {input_number} {input_unit} is equal to {output_number} {output_unit}.");
//     exit = prompt("Would you like to do more conversions? > ");
//     if exit != 'yes' {
//         break;
//     }
// }

var convert_to_meters = {"feet in meter": 3.2804, "ft": .3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": .9144, "in": .0254, "cm": .01, "mm": .001};

let unitInput = document.getElementById("unitInput");
let unitSelect = document.getElementById("unitSelect");
let unitConvert = document.getElementById("unitConvert");
let convertPrint = document.getElementById("convertOutput");
let meters = parseFloat(unitInput * convert_to_meters[unitSelect]);
let convertOutput = parseFloat(meters / convert_to_meters[unitConvert]);

let convertButton = document.querySelector("#convertButton");
convertButton.addEventListener("click", function() {
    let unitInputField = document.getElementById("unitInput");
    let unitInput = unitInputField.value;
    // console.log(unitInput)
    let unitSelectField = document.getElementById("unitSelect");
    let unitSelect = unitSelectField.value;
    // console.log(unitSelect);
    meters = parseFloat(unitInput * convert_to_meters[unitSelect]);
    let unitConvertField = document.getElementById("unitConvert");
    let unitConvert = unitConvertField.value;
    // console.log(unitConvert);
    convertOutput = parseFloat(meters / convert_to_meters[unitConvert]);
    // console.log(convertOutput);
    let convertPrint = document.getElementById("convertPrint");
    convertPrint.innerText = `Your ${unitInput}${unitSelect} is now ${convertOutput}${unitConvert}`;
});