var groupmates = [
    {
        "name": "Элина",
        "group": "БСТ2256",
        "age": 24,
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": "Алексей",
        "group": "БСТ2256",
        "age": 24,
        "marks": [4, 4, 5, 4, 4]
    },
    {
        "name": "Владислав",
        "group": "БСТ2256",
        "age": 24,
        "marks": [3, 4, 3, 4, 3]
    },
    {
        "name": "Дмитрий",
        "group": "БСТ2255",
        "age": 22,
        "marks": [4, 5, 4, 4, 5]
    },
    {
        "name": "Ольга",
        "group": "БСТ2255",
        "age": 23,
        "marks": [3, 4, 4, 3, 4]
    },
    {
        "name": "Иван",
        "group": "БСТ2255",
        "age": 21,
        "marks": [5, 5, 4, 5, 5]
    },
    {
        "name": "Мария",
        "group": "БСТ2257",
        "age": 25,
        "marks": [4, 4, 4, 5, 4]
    },
    {
        "name": "Никита",
        "group": "БСТ2257",
        "age": 26,
        "marks": [3, 3, 4, 3, 3]
    },
    {
        "name": "Светлана",
        "group": "БСТ2257",
        "age": 27,
        "marks": [5, 5, 5, 5, 4]
    }
];

console.log(groupmates);

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
};

var printStudents = function(students){
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 10),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );

    for (var i = 0; i < students.length; i++){
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 10),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'], 20)
        );
    }

    console.log('\n');
};

printStudents(groupmates);

var selectStudentsByGroup = function(spisok, groupName) {
    var resultList = [];

    for (var j = 0; j < spisok.length; j++) {
        if (spisok[j]['group'] == groupName) {
            resultList.push(spisok[j]);
        }
    }

    return resultList;
};

var bst2256Students = selectStudentsByGroup(groupmates, "БСТ2256");
printStudents(bst2256Students);