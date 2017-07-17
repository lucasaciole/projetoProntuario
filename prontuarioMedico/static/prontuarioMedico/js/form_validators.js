/**
 * Created by felipequecole on 15/07/17.
 */
        var $seuCampoCpf = $("#cpf");
        $seuCampoCpf.mask('000.000.000-00', {reverse: true});

        var $seuCEP = $("#id_cep");
        $seuCEP.mask('00000-000', {reverse: true});

         $("#id_telefone").mask("(00) 00000-0009", {reverse:true});
         $("#id_telefone2").mask("(00) 00000-0009", {reverse:true});

         $('#id_rg').mask("99.999.999-9", {reverse:true});
        //
        // var $campoNascimento = $("#id_datanascimento");
        // $campoNascimento.mask('00-00-0000', {reverse:true});