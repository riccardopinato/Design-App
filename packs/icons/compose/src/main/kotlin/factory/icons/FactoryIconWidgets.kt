package factory.icons

import androidx.compose.foundation.layout.sizeIn
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.LocalContentColor
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp

/**
 * Thin Material 3 Icon wrapper with the canonical Factory icon vocabulary.
 *
 * Use null contentDescription only for genuinely decorative instances;
 * meaningful status icons require a localized description.
 */
@Composable
fun FactoryIcon(
    key: FactoryIconKey,
    contentDescription: String?,
    modifier: Modifier = Modifier,
    tint: Color = LocalContentColor.current,
) {
    Icon(
        imageVector = key.materialImageVector(),
        contentDescription = contentDescription,
        modifier = modifier,
        tint = tint,
    )
}

/**
 * Accessible icon-only action. Minimum touch target is 48dp.
 * Description must be non-empty and localized by the consuming app.
 */
@Composable
fun FactoryIconButton(
    key: FactoryIconKey,
    contentDescription: String,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    enabled: Boolean = true,
) {
    require(contentDescription.isNotBlank()) {
        "An interactive icon needs a localized contentDescription."
    }
    IconButton(
        onClick = onClick,
        enabled = enabled,
        modifier = modifier.sizeIn(minWidth = 48.dp, minHeight = 48.dp),
    ) {
        FactoryIcon(key = key, contentDescription = contentDescription)
    }
}
