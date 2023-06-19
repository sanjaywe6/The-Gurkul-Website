$(document).ready(function () {

    function show_message(msg) {
        $('#absoluteMsg_outer').css('visibility', 'unset')
        $('#absoluteMsg_outer').addClass('absoluteMsg_outer_incoming')
        $('#show_msg').text(msg)

    }

    $('#hide_msg').click(function () {
        $('#absoluteMsg_outer').css('visibility', 'hidden')
        $('#absoluteMsg_outer').removeClass('absoluteMsg_outer_incoming')
    })

    function update_question_id_in_form() {
        $.ajax({
            url: '/gurkul_test/test_series/GTA_questions/get__GTA_question_form',
            type: 'post',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                get_empty_question_id: 'True'
            },

            success: function (data) {
                $('#current_question_id').text(data.next_id)
            }
        })
    }

    function show_questions(question_category, language, board, standard, subject, qtype, total_len) {
        $.ajax({
            url: '/gurkul_test/test_series/GTA_questions/return_gta_question',
            type: 'post',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                input_category: question_category,
                input_language: language,
                input_board: board,
                input_standard: standard,
                input_subject: subject,
                input_qtype: qtype,

            },

            success: function (data) {
                questions = data.all_question

                lst_question = `<div style="display: flex; justify-content:center; align-items:center; flex-wrap:wrap; background-image: linear-gradient(90deg,black,red,green,black); width: 100%; min-height: 60px;justify-items: center;align-items: center;padding:10px;border:1px solid black; border-radius:8px;">
                
                    <div><p id="show_len" class="btn btn-primary" style="margin: 10px;">Total Questions: </p></div>
                    <div><p id="show_lang" class="btn btn-primary" style="margin: 10px;">Language: </p></div>
                    <div><p id="show_board" class="btn btn-primary" style="margin: 10px;">Board: </p></div>
                    <div><p id="show_standard" class="btn btn-primary" style="margin: 10px;">Standard: </p></div>
                    <div><p id="show_subject" class="btn btn-primary" style="margin: 10px;">Subject: </p></div>
                    <div><p id="show_qtype" class="btn btn-primary" style="margin: 10px;">Question Type: </p></div>
                    <div><p id="show_all_questions" class="btn btn-danger" style="margin: 10px;">Show All Questions</p></div>
                
                    </div>`;

                if (questions.length < total_len) {
                    questions_length = questions.length
                }
                else {
                    questions_length = total_len
                }

                var iter = 0

                if (qtype == 'MCQ') {
                    for (let index = 0; index < questions_length; index++) {
                        const element = questions[index];
                        iter++

                        lst_question += `
                            <div
                            style="background-color: yellow; padding: 10px; border: 2px solid red;      border-radius: 10px; margin: 30px 0px 0px 0px; box-shadow: 0px 0px 20px red;">

                            <div style="display: grid; grid-template-columns: 40px 1fr 130px;padding: 10px; background-color: #f600ff; border: 1px solid black;       border-radius: 8px;">
                                <div>
                                    <h5 ><b style="color: black;">${index + 1}. </b></h5>
                                </div>
                                <div>
                                    <p style="color: rgb(0, 0, 0); font-size: 18px;">${element.question}</p>
                                </div>

                                <div style="display:flex; align-items:end;">
                                    <h5 ><b style="color: #ffeb00;"> ${element.id}</b></h5>
                                </div>


                            </div>
                            <div
                            style="display: grid; grid-template-columns: 1fr 1fr;       grid-template-rows: 1fr 1fr; padding: 10px; grid-column-gap: 10px;">
                            <div style="display: grid; grid-template-columns: 50px 1fr;         background-color: blue;
                            color: white;
                            align-items: center;
                            border: 1px solid red;
                            border-radius: 9px;
                            margin-bottom: 10px;
                                padding: 10px;
                            ">
                                    <div>
                                        <h5 style=" margin: 0px;">(A)</h5>
                                    </div>
                                    <div>
                                        <p style="font-size: 17px; margin: 0px;">${element.option_1}
                                            </p>
                                    </div>
                                </div>
                                <div style="display: grid; grid-template-columns: 50px 1fr;         background-color: blue;
                                color: white;
                                align-items: center;
                                border: 1px solid red;
                                border-radius: 9px;
                                margin-bottom: 10px;
                                padding: 10px;
                            ">
                            <div>
                                        <h5  style=" margin: 0px;">(B)</h5>
                                    </div>
                                    <div>
                                        <p style="font-size: 17px; margin: 0px;">${element.option_2}
                                            </p>
                                    </div>
                                </div>
                                <div style="display: grid; grid-template-columns: 50px 1fr;         background-color: blue;
                                color: white;
                                align-items: center;
                                border: 1px solid red;
                                border-radius: 9px;
                                margin-bottom: 10px;
                            padding: 10px;
                        ">
                                <div>
                                    <h5 style=" margin: 0px;">(C)</h5>
                                    </div>
                                    <div>
                                        <p style="font-size: 17px; margin: 0px;">${element.option_3}
                                            </p>
                                </div>
                                </div>
                            <div style="display: grid; grid-template-columns: 50px 1fr;      background-color: blue;
                            color: white;
                            align-items: center;
                            border: 1px solid red;
                            border-radius: 9px;
                            margin-bottom: 10px;
                            padding: 10px;
                        ">
                                <div>
                                    <h5 style=" margin: 0px;">(D)</h5>
                                    </div>
                                <div>
                                    <p style="font-size: 17px; margin: 0px;">${element.option_4}
                                    </p>
                                </div>
                            </div>
                        </div>
                    
                        <div class="edit_btn_div" style="display: flex; justify-content: space-between; align-items:center;">

                            <div>
                                <p style="background-color: white; color: red; font-size: 20px;  padding: 7px; border: 1px solid red; border-radius: 7px; margin:         0px;">Correct Answer: <b> ${element.answer_option}</b></p>
                            </div>
                            <div>
                                <button class="btn btn-danger btn_edit" data-qid="${element.id}">Edit</   button>
                                    </div>
                                    
                                    </div>
                                    
                                    </div>
                                    
                                    `
                    }

                }

                else if (qtype == 'STQ' || qtype == 'LTQ' || qtype == 'VLTQ') {

                    for (let index = 0; index < questions_length; index++) {
                        const element = questions[index];
                        iter++

                        lst_question += `
                            <div
                            style="background-color: yellow; padding: 10px; border: 2px solid red;      border-radius: 10px; margin: 30px 0px 0px 0px; box-shadow: 0px 0px 20px red;">

                            <div style="display: grid; grid-template-columns: 40px 1fr 130px;padding: 10px; background-color: #f600ff; border: 1px solid black;border-radius: 8px;">
                                <div>
                                    <h5 ><b style="color: black;">${index + 1}. </b></h5>
                                </div>
                                <div>
                                    <p style="color: rgb(0, 0, 0); font-size: 18px;">${element.question}</p>
                                </div>console.log('show')

                                <div style="display:flex; align-items:end;">
                                    <h5 ><b style="color: #ffeb00;"> ${element.id}</b></h5>
                                </div>


                            </div>
                    
                        <div class="edit_btn_div"  style="display: flex; justify-content: space-between; align-items:center; margin-top:10px;">

                            <div>
                                <p style="background-color: white; color: red; font-size: 20px;  padding: 7px; border: 1px solid red; border-radius: 7px; margin:         0px;">Correct Answer: <b> ${element.answer_option}</b></p>
                            </div>
                            <div>
                                <button class="btn btn-danger btn_edit" data-qid="${element.id}">Edit</button>
                                    </div>
                                    
                                    </div>
                                    
                                    </div>
                                    
                                    `
                    }

                }

                // filling all question in html tag
                $('#all_filtered_question').html(lst_question)

                $('#show_len').text(`Total Questions: ${questions.length}`)
                $('#show_len').attr('data-question_len',`${questions.length}`)
                $('#show_lang').text(`Language: ${language}`)
                $('#show_board').text(`Board: ${board}`)
                $('#show_standard').text(`Standard: ${standard}`)
                $('#show_subject').text(`Subject: ${subject}`)
                $('#show_qtype').text(`Question Type: ${qtype}`)

                // code to hide/unhide show more question initiall logically
                var int_len = parseInt(total_len) + 10
                if (questions.length > total_len && iter + 1 < questions.length) {
                    if (int_len < parseInt(data.questions_len)) {
                        $('#more_questions').attr('data-more_questions', `${int_len}`)

                    }
                    else {
                        $('#more_questions').attr('data-more_questions', data.questions_len)
                    }

                    $('#more_questions').css('display', 'unset')
                    $('#more_questions').attr('data-category', question_category)
                    $('#more_questions').attr('data-language', language)
                    $('#more_questions').attr('data-board', board)
                    $('#more_questions').attr('data-standard', standard)
                    $('#more_questions').attr('data-subject', subject)
                    $('#more_questions').attr('data-qtype', qtype)


                }

            }


        })


    }

    $('#display_fields').on('submit', '#gta_questions_form', function (e) {
        e.preventDefault()

        form_status = $('#form_status').attr('data-status')
        qid = $('#form_status').attr('data-qid')

        $.ajax({
            url: '/gurkul_test/test_series/GTA_questions/get__GTA_question_form',
            type: 'post',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                form_status: form_status,
                qid: qid,
                input_category: $('#input_category').val(),
                input_language: $('#input_language').val(),
                input_board: $('#input_board').val(),
                input_standard: $('#input_standard').val(),
                input_subject: $('#input_subject').val(),
                input_qtype: $('#input_qtype').val(),

                // question value
                input_question: $('#input_question').val(),

                radio_option: $("input[type='radio'][name='option_for_question']:checked").val(),

                // options value
                input_option_1: $('#input_option_1').val(),

                input_option_2: $('#input_option_2').val(),

                input_option_3: $('#input_option_3').val(),

                input_option_4: $('#input_option_4').val(),

                // answer input
                input_answer: $('#input_answer').val(),

            },

            success: function (data) {
                msg = data.status['msg']
                show_message(msg)
                code = data.status['code']
                if (code == 200) {
                    show_questions(data.input_category, data.input_language, data.input_board, data.input_standard, data.input_subject, data.input_qtype, 5)

                    $('#form_status').attr('data-status', 'new')
                    $('#form_status').attr('data-qid', 0)
                    $('#input_question').val('')
                    $('#radio_option_1').prop('checked', false)
                    $('#radio_option_2').prop('checked', false)
                    $('#radio_option_3').prop('checked', false)
                    $('#radio_option_4').prop('checked', false)
                    $('#input_option_1').val('')
                    $('#input_option_2').val('')
                    $('#input_option_3').val('')
                    $('#input_option_4').val('')
                    $('#input_option_4').val('')
                    $('#input_answer').val('')
                    update_question_id_in_form()



                }


            }
        })

    })

    // code for showing more questions
    $('#more_questions').click(function () {
        len = $(this).attr('data-more_questions')
        category = $(this).attr('data-category')
        language = $(this).attr('data-language')
        board = $(this).attr('data-board')
        standard = $(this).attr('data-standard')
        subject = $(this).attr('data-subject')
        qtype = $(this).attr('data-qtype')
        show_questions(category, language, board, standard, subject, qtype, len)
    })

    function get_question_with_id(id) {
        $.ajax({
            url: '/gurkul_test/test_series/GTA_questions/return_question_with_id',
            type: 'post',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                qid: id
            },
            success: function (data) {
                window.scrollTo(0, 0)
                var question = data.question
                $('#current_question_id').text(question[0].id)
                $('#form_status').attr('data-status', 'old')
                $('#form_status').attr('data-qid', question[0].id)
                $(`#input_category option[value='${question[0].question_category}']`).attr('selected', 'selected')
                $(`#input_language option[value='${question[0].language}']`).attr('selected', 'selected')
                $(`#input_board option[value='${question[0].board}']`).attr('selected', 'selected')
                $(`#input_standard option[value='${question[0].standard}']`).attr('selected', 'selected')
                $(`#input_subject option[value='${question[0].subject}']`).attr('selected', 'selected')
                $(`#input_qtype option[value='${question[0].qtype}']`).attr('selected', 'selected')
                $('#input_question').val(question[0].question)
                $(`#radio_option_${question[0].answer_option}`).prop('checked', true)
                $('#input_option_1').val(question[0].option_1)
                $('#input_option_2').val(question[0].option_2)
                $('#input_option_3').val(question[0].option_3)
                $('#input_option_4').val(question[0].option_4)
                $('#input_option_4').val(question[0].option_4)
                $('#input_answer').val(question[0].answer)

            }
        })
    }

    $('#all_filtered_question').on('click', '.btn_edit', function (e) {
        var id = $(this).attr('data-qid')
        get_question_with_id(id)

    })


    $('#show_question_with_options').click(function () {
        category = $('#input_category').val()
        language = $('#input_language').val()
        board = $('#input_board').val()
        standard = $('#input_standard').val()
        subject = $('#input_subject').val()
        qtype = $('#input_qtype').val()
        show_questions(category, language, board, standard, subject, qtype, 10)
    })

    // js for showing all question at a time
    $('#all_filtered_question').on('click', '#show_all_questions', function () {
        question_len=$('#show_len').attr('data-question_len')
        show_questions(category, language, board, standard, subject, qtype, question_len)
    })


    // js to block input when slecting options
    $('#input_category').click(function(){
        category_val=$('#input_category').val()
        if(category_val=='Comp'){
            $('#input_board').val('Other')
            $('#input_board').prop('disabled',true)
        }
        if(category_val=='Acad' || category_val=='Other'){
            $('#input_board').prop('disabled',false)
        }
    })

    $('#input_qtype').click(function(){
        qtype_val=$(this).val()  
        if(qtype_val=='STQ' || qtype_val=='LTQ' || qtype_val=='VLTQ'){
            for (let index = 1; index < 5; index++) {
                $(`#input_option_${index}`).prop('disabled',true)
                $(`#radio_option_${index}`).prop('checked',false)
                $(`#radio_option_${index}`).prop('disabled',true)
            }
            $("input[type='radio'][name='option_for_question']:checked").val('Other')
        } 
        else if(qtype_val=='MCQ'){
            for (let index = 1; index < 5; index++) {
                $(`#input_option_${index}`).prop('disabled',false)
                $(`#radio_option_${index}`).prop('disabled',false)
            }
        } 
    
    })




})